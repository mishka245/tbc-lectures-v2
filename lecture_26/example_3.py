from datetime import datetime

import requests

API_KEY = "{}"  # do not do like this, use environment variables

lat, lon = 42.161960, 42.344841
URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(URL)
print("Status code", response.status_code)

data = response.json()
print("Body", data)

forecasts = data["list"]
ordered_forecasts = sorted(forecasts, key=lambda x: x["dt"])

for forcast in ordered_forecasts:
    print(forcast["dt"],datetime.fromtimestamp(forcast["dt"]).isoformat(),  forcast["main"]["temp"])
    # timestamp to datetime




