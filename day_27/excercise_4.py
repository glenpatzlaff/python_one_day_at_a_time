import requests

# Attempt to fetch data from an invalid endpoint
url = "https://jsonplaceholder.typicode.com/invalid_endpoint"

try:
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code == 404:
        print("Error: The requested endpoint was not found.")
    elif response.status_code != 200:
        print(f"Error: The request failed with status code {response.status_code}.")
    else:
        print("The request was successful.")
except requests.exceptions.RequestException as e:
    # Catch any exceptions thrown during the request
    print(f"An error occurred: {e}")
