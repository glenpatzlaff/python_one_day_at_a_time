import requests
from bs4 import BeautifulSoup

# Start with the URL of the first page of the blog
start_url = 'https://example.com/blog'

def get_blog_titles(url):
    titles = []
    while url:
        try:
            # Fetch the content of the webpage
            response = requests.get(url)
            response.raise_for_status()  # Ensure we notice bad responses

            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract blog titles
            # Update '.blog-title' according to the actual class or element of blog titles
            for title in soup.select('.blog-title'):
                titles.append(title.text.strip())

            # Find the link to the next page
            # Update '.next-page' to the actual class or element of the next page link
            next_page = soup.select_one('.next-page')

            url = next_page['href'] if next_page else None  # Update URL or end loop
        except requests.RequestException as e:
            print(f'Error fetching the webpage: {e}')
            break  # Exit loop on error

    return titles

# Execute the function
blog_titles = get_blog_titles(start_url)

# Print results
print(f'Total blog titles extracted: {len(blog_titles)}')
for title in blog_titles:
    print(title)
