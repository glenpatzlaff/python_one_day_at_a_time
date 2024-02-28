import requests

# Define the URL for the JSONPlaceholder /users endpoint
url = 'https://jsonplaceholder.typicode.com/users'

# Make a GET request to fetch the list of users
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    users = response.json()

    # Loop through each user and print their name and company name
    for user in users:
        user_name = user['name']
        company_name = user['company']['name']
        print(f"User: {user_name}, Company: {company_name}")
else:
    print("Failed to fetch data from the server.")
