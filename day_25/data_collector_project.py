import requests
from bs4 import BeautifulSoup

url = 'https://example.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='product')
for product in products:
    name = product.find('h2', class_='product-name').text.strip()
    price = product.find('span', class_='price').text.strip()
    # Extract other data points similarly

   next_page = soup.find('a', text='Next')
   if next_page:
       next_page_url = next_page['href']
       # Repeat the scraping process for the next page

import pandas as pd

data = {
    'Name': [name1, name2, ...],
    'Price': [price1, price2, ...],
    # Include other data columns
}
df = pd.DataFrame(data)
df.to_csv('products.csv', index=False)

