import requests

# Replace with your GitHub token and repo details
GITHUB_TOKEN = 'github-access-key'
REPO_OWNER = 'OBEDPoP'
REPO_NAME = 'devops-project'

# GitHub API URL
url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Create an issue
issue_data = {
    'title': 'First Issue',
    'body': 'This is an automated issue created using the GitHub API.'
}

response = requests.post(url, json=issue_data, headers=headers)

if response.status_code == 201:
    print("Issue created successfully!")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.json())
