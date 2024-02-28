import requests

# Define the URL for the JSONPlaceholder /posts endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Make a GET request to fetch the data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the title of the first post
    first_post_title = data[0]['title']

    # Print the title to the console
    print("Title of the first post:", first_post_title)
else:
    print("Failed to fetch data from the server.")
