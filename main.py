import os
import requests
from twilio.rest import Client
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")


parameters = {
    "lat": 11.234130,
    "lon": 75.795502,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    weatherid = hour_data["weather"][0]["id"]
    if weatherid < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body = "When it rains, it pours. Bring an Umbrella. ☔",
        to='whatsapp:+4917647098469'
    )
    print(message.status)


