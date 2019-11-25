import pandas as pd


data = pd.read_csv("weather_data.csv")
print(data.head(10))

print(data.shape)

print(data[:2])
print(data[2:])
print(data[::-1])

print(data.columns)
print(data["day"])

print(data[["day" , "event"]])

print(data["temperature"].max())
print(data["temperature"].min())
print(data["temperature"].mean())
print(data.describe())

print(data[data ["temperature"] > 20])

print(data.set_index("day"))





