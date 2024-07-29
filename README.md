# DRF Weather API

This is a simple weather API built using Django Rest Framework (DRF). It provides current weather information based on the input location name.
api: weatherapi
url: https://www.weatherapi.com/
## Features

- Retrieve current weather data for a specified location.
- Utilizes an external weather API to fetch real-time weather information.



input example
{
  "name": "nepal"
}

output example 
{
  "data": {
    "location": {
      "name": "Kathmandu",
      "region": "",
      "country": "Nepal",
      "lat": 27.72,
      "lon": 85.32,
      "tz_id": "Asia/Kathmandu",
      "localtime_epoch": 1722269956,
      "localtime": "2024-07-29 22:04"
    },
    "current": {
      "last_updated_epoch": 1722269700,
      "last_updated": "2024-07-29 22:00",
      "temp_c": 22.2,
      "temp_f": 72.0,
      "is_day": 0,
      "condition": {
        "text": "Light rain shower",
        "icon": "//cdn.weatherapi.com/weather/64x64/night/353.png",
        "code": 1240
      },
      "wind_mph": 2.2,
      "wind_kph": 3.6,
      "wind_degree": 66,
      "wind_dir": "ENE",
      "pressure_mb": 1005.0,
      "pressure_in": 29.67,
      "precip_mm": 0.45,
      "precip_in": 0.02,
      "humidity": 91,
      "cloud": 64,
      "feelslike_c": 24.7,
      "feelslike_f": 76.4,
      "windchill_c": 22.2,
      "windchill_f": 72.0,
      "heatindex_c": 24.7,
      "heatindex_f": 76.4,
      "dewpoint_c": 20.6,
      "dewpoint_f": 69.1,
      "vis_km": 10.0,
      "vis_miles": 6.0,
      "uv": 1.0,
      "gust_mph": 6.7,
      "gust_kph": 10.8
    }
  }
}
