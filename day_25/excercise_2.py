import requests
from bs4 import BeautifulSoup

# Replace this URL with the URL of the webpage you want to scrape
books_url = 'https://example.com/books'

try:
    # Fetch the content of the webpage
    response = requests.get(books_url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize a list to store book data
    books_data = []

    # Assuming each book entry is contained in an element with a specific class
    # Update '.book-entry' to the correct class or element identifier
    for book in soup.select('.book-entry'):
        # Extract title and price assuming specific class names
        # These selectors must be updated according to the site's structure
        title = book.select_one('.book-title').text.strip()
        price = book.select_one('.book-price').text.strip()

        # Store the extracted information
        books_data.append({'title': title, 'price': price})

    # Print the extracted information
    print(books_data)
except requests.RequestException as e:
    print(f'Error fetching the webpage: {e}')
