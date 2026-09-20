import requests

def get_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        submitStats { acSubmissionNum { difficulty count } }
        profile { ranking }
      }
    }
    """
    variables = {"username": username}
    res = requests.post(url, json={"query": query, "variables": variables})

    if res.status_code == 200:
        data = res.json()
        try:
            stats = data['data']['matchedUser']['submitStats']['acSubmissionNum']
            total = stats[0]['count']
            return {"total_solved": total, "ranking": data['data']['matchedUser']['profile']['ranking']}
        except:
            return None
    return None

# Test
# print(get_leetcode_data("leetcode")) 
