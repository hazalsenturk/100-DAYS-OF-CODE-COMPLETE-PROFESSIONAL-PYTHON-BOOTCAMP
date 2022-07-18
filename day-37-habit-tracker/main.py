import requests
from datetime import datetime

USERNAME = "hazal"
TOKEN = "%lksh(ncmd=*wdqQ(6f3h7ı9p3".encode('utf-8')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
        "id": "graph1",
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
to_delete = datetime(year=2020, month=3, day=15)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{to_delete.strftime('%Y%m%d')}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

new_pixel_data = {
    "quantity": "4.5"
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
#response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
#response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
