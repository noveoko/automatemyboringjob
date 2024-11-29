# Confluence API Client

A Python wrapper for interacting with Confluence Cloud API using access tokens. This client provides an easy-to-use interface for common Confluence operations such as creating, reading, updating, and deleting pages.

## Features

- Simple authentication using access tokens
- Create and manage pages
- Search content using CQL
- Retrieve space content
- Update existing pages
- Delete pages
- Type hints for better code completion and documentation

## Installation

1. Install the required package:

```bash
pip install atlassian-python-api
```

2. Clone this repository or copy the `confluence_client.py` file to your project.

## Configuration

You'll need:
1. Your Confluence Cloud URL (e.g., 'https://your-domain.atlassian.net')
2. An API token from Atlassian

To generate an API token:
1. Log in to https://id.atlassian.com/manage/api-tokens
2. Click "Create API token"
3. Give it a name and copy the token value

## Usage

### Initialize the Client

```python
from confluence_client import ConfluenceClient

confluence = ConfluenceClient(
    url="https://your-domain.atlassian.net",
    token="your-access-token"
)
```

### Create a New Page

```python
new_page = confluence.create_page(
    space_key="TEAM",
    title="My New Page",
    content="<p>Hello, World!</p>"
)
```

### Get Page Content

```python
content = confluence.get_page_content(page_id="123456")
```

### Update a Page

```python
updated_page = confluence.update_page(
    page_id="123456",
    title="Updated Page Title",
    content="<p>Updated content</p>"
)
```

### Search Content

```python
results = confluence.search_content("text ~ 'search term'")
```

### Get Space Content

```python
pages = confluence.get_space_content(
    space_key="TEAM",
    content_type="page",
    limit=50
)
```

### Delete a Page

```python
confluence.delete_page(page_id="123456")
```

## Content Format

Content in Confluence uses the "storage format" (a subset of HTML). When creating or updating pages, provide content in this format. For example:

```python
content = """
<p>This is a paragraph</p>
<h1>This is a heading</h1>
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
</ul>
"""
```

## Error Handling

The client uses the underlying `atlassian-python-api` library's error handling. Common exceptions include:
- `HTTPError`: For HTTP-related errors
- `ApiError`: For Confluence API-specific errors

It's recommended to wrap API calls in try-except blocks:

```python
try:
    page = confluence.create_page(space_key="TEAM", title="Test", content="<p>Content</p>")
except Exception as e:
    print(f"Error creating page: {str(e)}")
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this code in your projects.

## Security Notes

- Never commit your API token to version control
- Consider using environment variables or a secure configuration management system for tokens
- The API token has access to your Confluence instance with the same permissions as your user account

## Dependencies

- Python 3.6+
- atlassian-python-api