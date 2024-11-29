# Automation & Utility Tools Collection

A comprehensive collection of automation tools, scripts, and utilities for increasing productivity and automating repetitive tasks.

## 🤖 Automation

### Confluence Automation
Tools for automating Confluence documentation tasks.
```python
# Example: Batch update Confluence pages
from confluence_automation import update_pages

update_pages(
    space="TEAM",
    template="release-notes",
    updates=[{"title": "Release 1.0", "content": content}]
)
```

### Google Workspace Automation
Scripts for automating Google Workspace operations.
```javascript
// Example: Batch fetch Google search results
const results = await fetchSearchResults({
    query: "site:example.com important topic",
    maxResults: 100
});
```

### MBOX Automation
Tools for processing and analyzing email archives.
```python
# Example: Full text search across email archives
from mbox_automation import search_emails

results = search_emails(
    mbox_path="archives/2024.mbox",
    query="project deadline"
)
```

### Desktop Automation
Scripts for automating desktop workflows and tasks.
```python
# Example: Automated file organization
organize_downloads(
    rules={
        "*.pdf": "Documents/PDFs",
        "*.jpg": "Pictures"
    }
)
```

## 🛠️ Tools

### Regex Generator
Interactive tool for generating and testing regular expressions.
```python
# Example: Generate regex for matching dates
pattern = generate_regex(
    examples=["2024-01-01", "2023-12-31"],
    pattern_type="date"
)
```

### Code Search
Advanced code search utilities with semantic understanding.
```python
# Example: Find similar code patterns
similar_code = search_codebase(
    pattern="database connection",
    similarity_threshold=0.8
)
```

### Duplicate File Removal
Smart duplicate file detection and removal.
```python
# Example: Remove duplicates while preserving originals
from remove_duplicates import cleanup

cleanup(
    directory="./photos",
    strategy="hash"  # or "content" or "name"
)
```

## 🌐 Web

### Ductube
Video management and processing utilities.
```python
# Example: Batch process videos
process_videos(
    input_dir="raw_videos",
    operations=["compress", "watermark"]
)
```

### Social Media Automation
Tools for managing social media presence.
```javascript
// Example: Moderate Facebook group
const moderationRules = {
    spam_keywords: ["buy now", "discount"],
    auto_approve: false
};
moderateGroup(groupId, moderationRules);
```

## �Media

### Image Processing
Collection of image manipulation and analysis tools.
```python
# Example: Generate image fingerprint
from simple_image_hash import hash_image

hash = hash_image("photo.jpg")
similar_images = find_similar(hash, threshold=0.9)
```

### Audio Processing
Tools for audio file manipulation, including ebook-to-audio conversion.
```python
# Example: Convert ebook to audiobook
from ebook_to_audiobook import convert

convert(
    input_file="book.pdf",
    output_format="mp3",
    voice="natural"
)
```

## 🔐 Security

### Send Secrets
Secure file and message transmission utilities.
```python
# Example: Encrypt and send sensitive data
from send_secrets import secure_send

secure_send(
    file_path="sensitive.doc",
    recipient="user@example.com",
    encryption="AES256"
)
```

### Dangerous Places
Security analysis and monitoring tools.
```python
# Example: Monitor network for suspicious activity
monitor_network(
    interfaces=["eth0"],
    alert_on=["port_scan", "unusual_traffic"]
)
```

## 🔧 Utils

### Semantic Search
Advanced search capabilities across various data types.
```python
# Example: Search across documentation
results = semantic_search(
    query="how to deploy application",
    corpus="./documentation",
    model="local"
)
```

### Domain Management
Tools for managing and monitoring domain portfolios.
```python
# Example: Check domain health
domain_status = check_domains([
    "example.com",
    "example.org"
], checks=["dns", "ssl", "uptime"])
```

## 📚 Learning
Documentation, guides, and learning resources for various technologies and career development.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/automation-tools.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.