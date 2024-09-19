###########################
# Mist API Code Steve Voto#
###########################
#!/usr/bin/python3

import json
import requests

	def submit_json(data_list):
    url = "https://api.mist.com/api/v1/orgs/b5235849-2d7a-49fd-8e9e-19e38c25e755/services"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token xxxxxxxxxxxxxxx'  # Replace with your API token leave Token in place and only change xxxxxxx's
    }

    # Iterate over each entry in the list and post it separately
    for data in data_list:
        response = requests.post(url, headers=headers, json=data)
        handle_response(response)

def handle_response(response):
    # Pretty print the response
    if response.status_code == 200:
        response_data = response.json()
        pretty_output = json.dumps(response_data, indent=4)
        print(f"Response: {pretty_output}")
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == "__main__":
    # Define the JSON data list with multiple entries
    json_data_list = [
    {
        "addresses": [
            "192.168.66.0/24"
        ],
        "specs": [
            {
                "protocol": "any"
            }
        ],
        "traffic_type": "default",
        "id": "ba3714ef-4ca6-4b53-b0c9-f0823c36889b",
        "name": "alaska-lan",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658942,
        "modified_time": 1723658942,
        "type": "custom"
    },
    {
        "addresses": [
            "172.16.128.0/30"
        ],
        "specs": [
            {
                "protocol": "any"
            }
        ],
        "traffic_type": "default",
        "id": "645aa91d-85f9-4966-bc07-4d93a72bb9a3",
        "name": "boston-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659023,
        "modified_time": 1723659023,
        "type": "custom"
    },
    {
        "addresses": [
            "172.26.128.0/30"
        ],
        "specs": [
            {
                "protocol": "any"
            }
        ],
        "traffic_type": "default",
        "id": "7da36a87-a1e1-423c-87f9-6b2540b21b8c",
        "name": "boston-lan2",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659048,
        "modified_time": 1723659048,
        "type": "custom"
    },
    {
        "addresses": [
            "192.168.63.0/24"
        ],
        "specs": [
            {
                "protocol": "any"
            }
        ],
        "traffic_type": "default",
        "id": "f0d44750-5776-4ff9-ad6d-2400f4a18864",
        "name": "dallas-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659083,
        "modified_time": 1723659083,
        "type": "custom"
    },
    {
        "addresses": [
            "192.168.64.0/24"
        ],
        "specs": [
            {
                "protocol": "any"
            }
        ],
        "traffic_type": "default",
        "id": "7c033371-ff8b-4d41-aa73-0b7e3b14cd5a",
        "name": "seattle-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659109,
        "modified_time": 1723659109,
        "type": "custom"
    },
    {
        "addresses": [
            "192.168.65.0/24"
        ],
        "specs": [
            {
                "protocol": "any"
            }
        ],
        "traffic_type": "default",
        "id": "a1d76f7e-2dbb-4824-9536-8cb2ef8add07",
        "name": "seattle-lan2",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659125,
        "modified_time": 1723659125,
        "type": "custom"
    },
    {
        "addresses": [
            "172.16.128.0/30"
        ],
        "specs": [
            {
                "protocol": "tcp",
                "port_range": "80-80"
            }
        ],
        "traffic_type": "default",
        "id": "abfdc893-0eea-4716-96ec-0a5aa0676250",
        "name": "http-boston-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659166,
        "modified_time": 1723659166,
        "type": "custom"
    },
    {
        "addresses": [
            "172.26.128.0/30"
        ],
        "specs": [
            {
                "protocol": "tcp",
                "port_range": "80-80"
            }
        ],
        "traffic_type": "default",
        "id": "42cb131d-1a43-4419-8fa9-2bbe029ed54e",
        "name": "http-boston-lan2",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723659741,
        "modified_time": 1723659741,
        "type": "custom"
    }
]

        # Add more entries as needed


    # Submit the JSON data list
    submit_json(json_data_list)
