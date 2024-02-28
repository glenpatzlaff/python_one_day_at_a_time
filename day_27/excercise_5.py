import requests

# Fetch the list of users
users_url = "https://jsonplaceholder.typicode.com/users"
users_response = requests.get(users_url)
users = users_response.json()

# Fetch the list of posts
posts_url = "https://jsonplaceholder.typicode.com/posts"
posts_response = requests.get(posts_url)
posts = posts_response.json()

# Count the number of posts for each user
user_post_counts = {user['id']: 0 for user in users}
for post in posts:
    user_post_counts[post['userId']] += 1

# Print each user's name and the total number of posts they've made
for user in users:
    print(f"{user['name']} has made {user_post_counts[user['id']]} posts.")
