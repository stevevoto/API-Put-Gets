###########################
# Mist API Code Steve Voto#
###########################
#!/usr/bin/env python
import json
import requests

def submit_json(data_list):
    url = "https://api.mist.com/api/v1/orgs/b5235849-2d7a-49fd-8e9e-19e38c25e755/sites"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token xxxxxxxxxxxx'  # Replace with your API token leave Token in place and only change xxxxxxx's
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
        "country_code": "US",
        "timezone": "America/Chicago",
        "address": "Dallas, TX, USA",
        "sitegroup_ids": [],
        "notes": "",
        "latlng": {
            "lat": 32.776664,
            "lng": -96.796988
        },
        "id": "8afd2184-b3a3-4a19-b4f5-6a2de48912a0",
        "name": "dallas",
        "org_id": "b5235849-2d7a-49fd-8e9e-19e38c25e755",
        "created_time": 1726598719,
        "modified_time": 1726666613,
        "rftemplate_id": null,
        "aptemplate_id": null,
        "secpolicy_id": null,
        "alarmtemplate_id": null,
        "networktemplate_id": null,
        "gatewaytemplate_id": "ae18ac3b-274c-47d8-8abc-edc34d8bc79e",
        "sitetemplate_id": null,
        "tzoffset": 1080
    },
    {
        "country_code": "US",
        "timezone": "America/Anchorage",
        "address": "Nome, AK, USA",
        "sitegroup_ids": [],
        "notes": "",
        "latlng": {
            "lat": 64.500591,
            "lng": -165.408641
        },
        "id": "61352a8e-3b10-4717-9a5a-3b3525b0b224",
        "name": "alaska",
        "org_id": "b5235849-2d7a-49fd-8e9e-19e38c25e755",
        "created_time": 1726598733,
        "modified_time": 1726666593,
        "rftemplate_id": null,
        "aptemplate_id": null,
        "secpolicy_id": null,
        "alarmtemplate_id": null,
        "networktemplate_id": null,
        "gatewaytemplate_id": "79135b21-faf6-4028-9a92-8dae812304ec",
        "sitetemplate_id": null,
        "tzoffset": 900
    },
    {
        "country_code": "US",
        "timezone": "America/Los_Angeles",
        "address": "Seattle, WA, USA",
        "sitegroup_ids": [],
        "notes": "",
        "latlng": {
            "lat": 47.606139,
            "lng": -122.332848
        },
        "id": "f73ce9e2-a36d-44bd-8bb4-4c4a18680407",
        "name": "seattle",
        "org_id": "b5235849-2d7a-49fd-8e9e-19e38c25e755",
        "created_time": 1726598708,
        "modified_time": 1726666585,
        "rftemplate_id": null,
        "aptemplate_id": null,
        "secpolicy_id": null,
        "alarmtemplate_id": null,
        "networktemplate_id": null,
        "gatewaytemplate_id": "f8c564d7-9f88-4f17-a5ad-c45e3b96971e",
        "sitetemplate_id": null,
        "tzoffset": 960
    },
    {
        "country_code": "US",
        "timezone": "America/New_York",
        "address": "Boston, MA, USA",
        "sitegroup_ids": [],
        "notes": "",
        "latlng": {
            "lat": 42.360082,
            "lng": -71.05888
        },
        "id": "321f6474-912e-4d29-aa98-b17e3c5bc7d5",
        "name": "boston",
        "org_id": "b5235849-2d7a-49fd-8e9e-19e38c25e755",
        "created_time": 1726598306,
        "modified_time": 1726598306,
        "rftemplate_id": null,
        "aptemplate_id": null,
        "secpolicy_id": null,
        "alarmtemplate_id": null,
        "networktemplate_id": null,
        "gatewaytemplate_id": null,
        "sitetemplate_id": null,
        "tzoffset": 1140
    },
    {
        "timezone": "UTC",
        "id": "df2f54ed-0cf9-40fa-9fb3-7611fb6e7df6",
        "name": "main_site",
        "org_id": "b5235849-2d7a-49fd-8e9e-19e38c25e755",
        "created_time": 1726597243,
        "modified_time": 1726597243,
        "rftemplate_id": null,
        "aptemplate_id": null,
        "secpolicy_id": null,
        "alarmtemplate_id": null,
        "networktemplate_id": null,
        "gatewaytemplate_id": null,
        "sitetemplate_id": null,
        "tzoffset": 0
    }
]

    # Add more entries as needed


    # Submit the JSON data list
    submit_json(json_data_list)
