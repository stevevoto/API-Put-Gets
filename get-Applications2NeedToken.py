###########################
# Mist API Code Steve Voto#
###########################
#!/usr/bin/env python3
import requests
import json

def get_org_id():
    """Prompt the user to enter the org_id."""
    org_id = input("Enter the org_id: ").strip()
    return org_id

def get_sites(org_id):
    """Fetch and print sites from the Mist API."""
    url = f"https://api.mist.com/api/v1/orgs/{org_id}/services"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token xxxxxxxxxx'  # Replace with your API token leave Token in place and only change xxxxxxx's
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        # Parse the response as JSON
        response_data = response.json()
        # Pretty-print the JSON output
        pretty_output = json.dumps(response_data, indent=4)
        print(pretty_output)
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == "__main__":
    org_id = get_org_id()
    get_sites(org_id)

