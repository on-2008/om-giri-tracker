import requests

def get_github_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data.get("name"),
            "repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "bio": data.get("bio")
        }
    else:
        return None

# Test karne ke liye
# print(get_github_data("torvalds"))