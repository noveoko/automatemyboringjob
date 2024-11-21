from atlassian import Confluence
import json
from typing import Optional, Dict, List

class ConfluenceClient:
    def __init__(self, url: str, token: str):
        """
        Initialize Confluence client with base URL and access token
        
        Args:
            url: Base URL of your Confluence instance (e.g., 'https://your-domain.atlassian.net')
            token: Access token for authentication
        """
        self.confluence = Confluence(
            url=url,
            token=token,
            cloud=True  # Set to False if using Server/Data Center version
        )
    
    def create_page(self, space_key: str, title: str, content: str, parent_id: Optional[str] = None) -> Dict:
        """
        Create a new Confluence page
        
        Args:
            space_key: Key of the space where page will be created
            title: Title of the new page
            content: Content in storage format (HTML)
            parent_id: Optional ID of parent page
            
        Returns:
            Dict containing created page information
        """
        return self.confluence.create_page(
            space=space_key,
            title=title,
            body=content,
            parent_id=parent_id,
            representation='storage'
        )
    
    def get_page_content(self, page_id: str) -> str:
        """
        Get content of a specific page
        
        Args:
            page_id: ID of the page to retrieve
            
        Returns:
            Page content in storage format
        """
        return self.confluence.get_page_by_id(
            page_id=page_id,
            expand='body.storage'
        )['body']['storage']['value']
    
    def update_page(self, page_id: str, title: str, content: str) -> Dict:
        """
        Update an existing page
        
        Args:
            page_id: ID of the page to update
            title: New title of the page
            content: New content in storage format
            
        Returns:
            Dict containing updated page information
        """
        return self.confluence.update_page(
            page_id=page_id,
            title=title,
            body=content,
            representation='storage'
        )
    
    def get_space_content(self, space_key: str, content_type: str = 'page', limit: int = 50) -> List[Dict]:
        """
        Get all content of a specific type from a space
        
        Args:
            space_key: Key of the space to search
            content_type: Type of content ('page', 'blogpost', etc.)
            limit: Maximum number of items to return
            
        Returns:
            List of content items
        """
        return self.confluence.get_all_pages_from_space(
            space=space_key,
            start=0,
            limit=limit,
            content_type=content_type
        )
    
    def delete_page(self, page_id: str) -> None:
        """
        Delete a page
        
        Args:
            page_id: ID of the page to delete
        """
        self.confluence.remove_page(page_id=page_id)
    
    def search_content(self, query: str, limit: int = 50) -> List[Dict]:
        """
        Search for content using CQL
        
        Args:
            query: CQL query string
            limit: Maximum number of results to return
            
        Returns:
            List of matching content items
        """
        return self.confluence.cql(query, limit=limit)

# Example usage
if __name__ == "__main__":
    # Initialize client
    confluence = ConfluenceClient(
        url="https://your-domain.atlassian.net",
        token="your-access-token"
    )
    
    # Create a new page
    new_page = confluence.create_page(
        space_key="TEAM",
        title="API Test Page",
        content="<p>This is a test page created via API</p>"
    )
    print(f"Created page with ID: {new_page['id']}")
    
    # Get content from the created page
    content = confluence.get_page_content(new_page['id'])
    print(f"Page content: {content}")
    
    # Update the page
    updated_page = confluence.update_page(
        page_id=new_page['id'],
        title="Updated API Test Page",
        content="<p>This content has been updated via API</p>"
    )
    print(f"Updated page version: {updated_page['version']['number']}")
    
    # Search for content
    results = confluence.search_content("text ~ 'API Test'")
    print(f"Found {len(results)} matching pages")