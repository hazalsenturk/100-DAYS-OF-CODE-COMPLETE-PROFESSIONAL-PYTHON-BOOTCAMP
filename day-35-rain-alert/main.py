#I did not signed up for twilio, but here is the code to send a text message via code
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "account key"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 41.008240,
    "lon": 28.978359,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hour_zero_id = weather_data["hourly"][0]["weather"][0]["id"]
weather_dict = weather_data["hourly"]
weather_id = [day_time["weather"][0]["id"] for day_time in weather_dict[:12]]

will_rain = False

for id in weather_id:
    if id <= 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https":os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.message \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from = "your_phone_number",
        to="reciever_phone_number",
    )

print(message.status)
