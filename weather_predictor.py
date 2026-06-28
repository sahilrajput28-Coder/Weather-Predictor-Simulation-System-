import random

days = int(input("How many days do you want to predict? "))

weather_list = [
    "Sunny ☀️",
    "Sunny ☀️",
    "Sunny ☀️",
    "Cloudy ☁️",
    "Cloudy ☁️",
    "Rainy 🌧️"
]

sunny_count = 0
cloudy_count = 0
rainy_count = 0

print("\n🌦️ Weather Forecast Simulation 🌦️\n")

for i in range(days):

    weather = random.choice(weather_list)

    if weather == "Sunny ☀️":
        temperature = random.randint(30, 40)
        advice = "Stay Hydrated 🥤"
        sunny_count += 1

    elif weather == "Cloudy ☁️":
        temperature = random.randint(24, 32)
        advice = "Nice Weather for Outdoors 🌤️"
        cloudy_count += 1

    else:
        temperature = random.randint(18, 26)
        advice = "Carry Umbrella ☔"
        rainy_count += 1

    humidity = random.randint(40, 90)

    wind_speed = random.randint(5, 25)

    alert = ""

    if temperature >= 38:
        alert = "⚠️ Heatwave Warning!"

    elif wind_speed >= 20:
        alert = "⚠️ Strong Winds Alert!"

    print("Day", i + 1, "→", weather,
          "| Temperature:", temperature, "°C",
          "| Humidity:", humidity, "%",
          "| Wind Speed:", wind_speed, "km/h",
          "| Advice:", advice,
          "|", alert)

print("\n📊 Weather Summary Report 📊")

print("Sunny Days:", sunny_count)
print("Cloudy Days:", cloudy_count)
print("Rainy Days:", rainy_count)
