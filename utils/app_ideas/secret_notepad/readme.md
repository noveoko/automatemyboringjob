# Secure Line-by-Line Encrypted Notepad

A bash-based secure notepad application that provides line-by-line encryption of text files. Each line is independently encrypted with its own salt, and only the line being actively edited is decrypted. This approach minimizes exposure of sensitive data and provides strong protection against unauthorized access.

## Security Features

- **Line-by-Line Encryption**: Each line is encrypted independently using AES-256-CBC
- **Individual Salt per Line**: Every line has its own unique salt to prevent pattern matching
- **High-Iteration PBKDF2**: Uses 1,000,000 iterations for key derivation to slow down brute-force attempts
- **Minimal Exposure**: Only decrypts the current line being edited
- **Secure Memory Handling**: Temporary files are securely wiped after use
- **No Full Decryption**: Whole file decryption is disabled by default
- **Password Protection**: Secure password input with no screen display

## Dependencies

- OpenSSL
- Bash
- Standard Unix tools (sed, nl)
- A text editor (defaults to vim, can be changed via $EDITOR environment variable)

## Installation

1. Download the script:
```bash
curl -O https://[your-repo]/secure_notepad.sh
```

2. Make it executable:
```bash
chmod +x secure_notepad.sh
```

## Usage

1. Start the application:
```bash
./secure_notepad.sh filename.txt
```

2. Enter your encryption password when prompted

3. Use the following commands:
   - `a`: Add a new line
   - `e`: Edit an existing line
   - `d`: Delete a line
   - `q`: Quit

## Security Considerations

1. **Password Strength**: Use a strong password as it's the primary defense against unauthorized access
2. **Backup Management**: Encrypted files cannot be recovered without the password
3. **Memory Security**: While the application attempts to minimize exposure, be aware of system memory constraints
4. **Temporary Files**: Located in /tmp and securely wiped, but be aware of system-specific security implications
5. **Editor Security**: The security of the edited content depends on the security of your chosen text editor

## Technical Details

### Encryption Specifications
- Algorithm: AES-256-CBC
- Key Derivation: PBKDF2
- Iterations: 1,000,000
- Salt Size: 32 bytes per line
- Format: `salt:encrypted_data` (base64 encoded)

### File Format
Each line in the file is stored in the following format:
```
[32-byte-hex-salt]:[base64-encoded-encrypted-data]
```

## Limitations

1. No built-in backup functionality
2. No password recovery mechanism
3. Performance may be slower on large files due to security measures
4. No concurrent access support

## Best Practices

1. Regularly backup your encrypted files
2. Store the password securely
3. Use different passwords for different sensitive files
4. Be aware of your system's security limitations
5. Consider the security of your working environment

## Contributing

Contributions are welcome! Please consider the following areas for improvement:
- Additional encryption algorithms
- Backup functionality
- Password strength checking
- File integrity verification
- Performance optimizations

## License

This software is provided under the MIT License. See LICENSE file for details.

## Security Warnings

1. This tool is designed for personal use and hasn't undergone formal security audit
2. The security of your data depends on the security of your system and password
3. No encryption is unbreakable - use appropriate additional security measures
4. Always maintain secure backups of important data

## Support

For issues, questions, or contributions, please:
1. Check existing issues in the repository
2. Create a new issue with detailed information
3. Follow security best practices when reporting bugs

## Version History

- 1.0.0: Initial release with basic encryption functionality
- 1.0.1: Added secure memory handling
- 1.0.2: Improved salt generation and handling

## Credits

Developed as a security-focused alternative to standard text editors, with inspiration from various secure storage solutions and encryption tools.