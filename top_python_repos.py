import requests
import plotly.express as px

# Make an API call to GitHub to retrieve information about Python repositories with more than 10,000 stars.
# API call to the   and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Check if the API response includes complete results or if there are incomplete results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Extract repository names and star counts from the API response.
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Create a bar chart using Plotly Express to visualize repository stars.
title = "Most-Starred Python Projects on GitHub"
lables = {'x': 'Repository',
          'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, labels=lables)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                   yaxis_title_font_size=20, title_text=title)

fig.update_traces(marker_color='DarkSlateGrey', marker_opacity=0.7)

fig.show()

