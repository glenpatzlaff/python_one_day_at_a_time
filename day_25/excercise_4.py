import requests
from bs4 import BeautifulSoup

# URL of the e-commerce product page
url = 'https://example.com/product-page'

def scrape_product_info(url):
    try:
        # Fetch the content of the product page
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product name, description, and price
        # Update the selectors according to the actual structure of your target webpage
        product_name = soup.select_one('.product-name').text.strip()
        product_description = soup.select_one('.product-description').text.strip()
        product_price = soup.select_one('.product-price').text.strip()

        # Clean and format the extracted data
        # Removing currency symbols and converting price to float
        clean_price = float(product_price.replace('$', '').replace(',', ''))

        return {
            'Name': product_name,
            'Description': product_description,
            'Price': clean_price
        }

    except requests.RequestException as e:
        print(f'Error fetching the webpage: {e}')
        return None

# Scrape and print product information
product_info = scrape_product_info(url)
if product_info:
    print(f"Product Name: {product_info['Name']}")
    print(f"Description: {product_info['Description']}")
    print(f"Price: ${product_info['Price']:.2f}")
