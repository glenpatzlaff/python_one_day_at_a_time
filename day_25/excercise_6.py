import requests
from bs4 import BeautifulSoup
import csv

# The URL of the webpage to scrape
url = 'https://example.com/real-estate-listings'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all listings on the page (adjust the selector as per your webpage's structure)
listings = soup.find_all('div', class_='listing')

# List to store cleaned data
cleaned_data = []

for listing in listings:
    # Extract the desired information
    title = listing.find('h2').text.strip()
    price = listing.find('p', class_='price').text.strip()
    location = listing.find('p', class_='location').text.strip()
    features = listing.find('ul').text.strip()  # Example: '3 bedrooms, 2 bathrooms'

    # Clean/format the data as necessary
    price = price.replace('$', '').replace(',', '')  # Remove dollar sign and commas
    price = float(price)  # Convert price to float
    features = features.split(',')  # Convert features string to list

    # Append the cleaned data to the list
    cleaned_data.append([title, price, location, *features])

# Write the cleaned data to a CSV file
with open('real_estate_listings.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Price', 'Location', 'Features'])
    # Write the data rows
    for row in cleaned_data:
        writer.writerow(row)

print("Data scraped and saved to real_estate_listings.csv")
