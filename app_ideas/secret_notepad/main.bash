#!/bin/bash

# Dependencies check
command -v openssl >/dev/null 2>&1 || { echo "Error: openssl required but not installed. Aborting." >&2; exit 1; }

# Configuration
TEMP_FILE="/tmp/secure_notepad_temp_$$"
trap 'rm -f "$TEMP_FILE" 2>/dev/null' EXIT
SALT_SIZE=32
ITERATIONS=1000000  # High iteration count for slow decryption
ALGORITHM="aes-256-cbc"

# Function to encrypt a single line
encrypt_line() {
    local line="$1"
    local password="$2"
    local salt=$(openssl rand -hex $SALT_SIZE)
    echo -n "$salt:"
    echo -n "$line" | openssl enc -$ALGORITHM -pbkdf2 -iter $ITERATIONS -salt -pass pass:"$password$salt" 2>/dev/null | base64
}

# Function to decrypt a single line
decrypt_line() {
    local encrypted="$1"
    local password="$2"
    local salt=$(echo "$encrypted" | cut -d: -f1)
    local data=$(echo "$encrypted" | cut -d: -f2 | base64 -d)
    echo "$data" | openssl enc -d -$ALGORITHM -pbkdf2 -iter $ITERATIONS -salt -pass pass:"$password$salt" 2>/dev/null
}

# Function to edit a single line
edit_line() {
    local line="$1"
    local password="$2"
    local decrypted=""
    
    if [ ! -z "$line" ]; then
        decrypted=$(decrypt_line "$line" "$password")
    fi
    
    echo -n "$decrypted" > "$TEMP_FILE"
    ${EDITOR:-vim} "$TEMP_FILE"
    local edited=$(cat "$TEMP_FILE")
    rm -f "$TEMP_FILE"
    
    if [ ! -z "$edited" ]; then
        encrypt_line "$edited" "$password"
    fi
}

# Main function
main() {
    local file="$1"
    
    if [ -z "$file" ]; then
        echo "Usage: $0 <filename>"
        exit 1
    fi
    
    # Create file if it doesn't exist
    touch "$file"
    
    # Get password
    read -s -p "Enter encryption password: " password
    echo
    
    while true; do
        clear
        echo "Secure Notepad - $file"
        echo "Commands: (a)dd line, (e)dit line, (d)elete line, (q)uit"
        echo "----------------------------------------"
        
        # Display encrypted file with line numbers
        nl -ba "$file"
        
        echo "----------------------------------------"
        read -p "Command: " cmd
        
        case $cmd in
            a)
                # Add new line
                new_line=$(edit_line "" "$password")
                if [ ! -z "$new_line" ]; then
                    echo "$new_line" >> "$file"
                fi
                ;;
            e)
                # Edit existing line
                read -p "Line number to edit: " line_num
                if [ -z "$line_num" ]; then
                    continue
                fi
                
                old_line=$(sed "${line_num}!d" "$file")
                if [ -z "$old_line" ]; then
                    echo "Invalid line number"
                    read -p "Press Enter to continue..."
                    continue
                fi
                
                new_line=$(edit_line "$old_line" "$password")
                sed -i "${line_num}c\\${new_line}" "$file"
                ;;
            d)
                # Delete line
                read -p "Line number to delete: " line_num
                if [ ! -z "$line_num" ]; then
                    sed -i "${line_num}d" "$file"
                fi
                ;;
            q)
                exit 0
                ;;
        esac
    done
}

main "$1"