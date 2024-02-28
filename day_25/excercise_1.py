import requests
from bs4 import BeautifulSoup

# Replace the URL below with the actual blog post URL you want to fetch
blog_url = 'https://example.com/blog-post'

try:
    # Fetch the content of the blog post
    response = requests.get(blog_url)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the post (assuming it's in a <title> tag or an <h1> tag)
    # You might need to adjust the selector based on the actual HTML structure of the blog
    title = soup.find('title').get_text(strip=True) or soup.find('h1').get_text(strip=True)

    # Extract the author's name (assuming there's a specific class or id that denotes the author's name)
    # This will also need to be adjusted based on the blog's HTML structure
    # Example: author = soup.find(class_='author-name').get_text(strip=True)
    # For demonstration, let's assume there's a placeholder:
    author = "Author's Name Placeholder"

    # Print the extracted information
    print(f'Title: {title}')
    print(f'Author: {author}')
except requests.RequestException as e:
    print(f'Error fetching the blog post: {e}')
