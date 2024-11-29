import sqlite3

# Function to perform full-text search on SQLite database
def perform_full_text_search(keyword):
    conn = sqlite3.connect('gmail_data.db')
    c = conn.cursor()

    # Perform full-text search
    c.execute('''SELECT * FROM emails_fts WHERE emails_fts MATCH ?''', (keyword,))
    results = c.fetchall()

    # Print search results
    for row in results:
        print(row)

    conn.close()

if __name__ == "__main__":
    keyword = "search_keyword"
    perform_full_text_search(keyword)
