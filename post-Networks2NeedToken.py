###########################
# Mist API Code Steve Voto#
###########################
#!/usr/bin/python3
import json
import requests

def submit_json(data_list):
    url = "https://api.mist.com/api/v1/orgs/b5235849-2d7a-49fd-8e9e-19e38c25e755/networks"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token xxxxxxxxxxxxx'  # Replace with your API token leave Token in place and only change xxxxxxx's
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
        "isolation": "true",
        "subnet": "192.168.66.0/24",
        "tenants": {},
        "internet_access": {
            "static_nat": {},
            "destination_nat": {}
        },
        "vpn_access": {
            "OrgOverlay": {
                "routed": "true",
                "no_readvertise_to_overlay": "false",
                "no_readvertise_to_lan_bgp": "false",
                "no_readvertise_to_lan_ospf": "false"
            }
        },
        "ip": "192.168.66.0",
        "prefix": "24",
        "routed_for_networks": [],
        "sourceNats": [],
        "destNats": [],
        "users": [],
        "disallow_mist_services": "false",
        "id": "89ff85c1-69ae-4f40-a250-ccff1a655ec8",
        "name": "alaska-lan",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658346,
        "modified_time": 1723658346
    },
    {
        "isolation": "true",
        "subnet": "172.16.128.0/30",
        "tenants": {},
        "internet_access": {
            "static_nat": {},
            "destination_nat": {}
        },
        "vpn_access": {
            "OrgOverlay": {
                "routed": "true",
                "no_readvertise_to_overlay": "false",
                "no_readvertise_to_lan_bgp": "false",
                "no_readvertise_to_lan_ospf": "false"
            }
        },
        "ip": "172.16.128.0",
        "prefix": "30",
        "routed_for_networks": [],
        "sourceNats": [],
        "destNats": [],
        "users": [],
        "disallow_mist_services": "false",
        "id": "d66d823a-76fd-4f94-a78d-737cdafd993f",
        "name": "boston-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658445,
        "modified_time": 1723658445
    },
    {
        "isolation": "true",
        "subnet": "172.26.128.0/30",
        "tenants": {},
        "internet_access": {
            "static_nat": {},
            "destination_nat": {}
        },
        "vpn_access": {
            "OrgOverlay": {
                "routed": "true",
                "no_readvertise_to_overlay": "false",
                "no_readvertise_to_lan_bgp": "false",
                "no_readvertise_to_lan_ospf": "false"
            }
        },
        "ip": "172.26.128.0",
        "prefix": "30",
        "routed_for_networks": [],
        "sourceNats": [],
        "destNats": [],
        "users": [],
        "disallow_mist_services": "false",
        "id": "b2ff73e9-b194-489b-96d2-dce9d6fe4c31",
        "name": "boston-lan2",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658533,
        "modified_time": 1723658533
    },
    {
        "isolation": "true",
        "subnet": "192.168.63.0/24",
        "tenants": {},
        "internet_access": {
            "static_nat": {},
            "destination_nat": {}
        },
        "vpn_access": {
            "OrgOverlay": {
                "routed": "true",
                "no_readvertise_to_overlay": "false",
                "no_readvertise_to_lan_bgp": "false",
                "no_readvertise_to_lan_ospf": "false"
            }
        },
        "ip": "192.168.63.0",
        "prefix": "24",
        "routed_for_networks": [],
        "sourceNats": [],
        "destNats": [],
        "users": [],
        "disallow_mist_services": "false",
        "id": "4a299423-5e33-495a-953e-0def1b6c8b54",
        "name": "dallas-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658571,
        "modified_time": 1723658571
    },
    {
        "isolation": "true",
        "subnet": "192.168.64.0/24",
        "tenants": {},
        "internet_access": {
            "static_nat": {},
            "destination_nat": {}
        },
        "vpn_access": {
            "OrgOverlay": {
                "routed": "true",
                "no_readvertise_to_overlay": "false",
                "no_readvertise_to_lan_bgp": "false",
                "no_readvertise_to_lan_ospf": "false"
            }
        },
        "ip": "192.168.64.0",
        "prefix": "24",
        "routed_for_networks": [],
        "sourceNats": [],
        "destNats": [],
        "users": [],
        "disallow_mist_services": "false",
        "id": "3bef268c-ee9b-413a-be7e-297448fb6482",
        "name": "seattle-lan1",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658590,
        "modified_time": 1723658590
    },
    {
        "isolation": "true",
        "subnet": "192.168.65.0/24",
        "tenants": {},
        "internet_access": {
            "static_nat": {},
            "destination_nat": {}
        },
        "vpn_access": {
            "OrgOverlay": {
                "routed": "true",
                "no_readvertise_to_overlay": "false",
                "no_readvertise_to_lan_bgp": "false",
                "no_readvertise_to_lan_ospf": "false"
            }
        },
        "ip": "192.168.65.0",
        "prefix": "24",
        "routed_for_networks": [],
        "sourceNats": [],
        "destNats": [],
        "users": [],
        "disallow_mist_services": "false",
        "id": "028c6ca3-20bc-4f8d-b640-d8bb2dbedc5e",
        "name": "seattle-lan2",
        "org_id": "b99e15b9-3457-4137-8a9d-b2272187c255",
        "created_time": 1723658610,
        "modified_time": 1723658610
    }
]
    # Add more entries as needed


    # Submit the JSON data list
    submit_json(json_data_list)
