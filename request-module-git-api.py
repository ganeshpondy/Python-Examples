import requests
import json

# Get the Repo details for User
request_info = requests.get("https://api.github.com/users/ganeshpondy/repos")

# Convert the details into JSON Format
project_details = request_info.json()

# Print the Details in FOR Loop
for project_items in project_details:
    print(f"Project name is {project_items['full_name']} \nProject URL is {project_items['url']}\n")
    
