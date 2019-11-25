import pandas as pd


weather_data = {
    "day" : ["1/1/2017" , "1/2/2017" , "1/3/2017"],
    "temperature " : [32 , 35 , 28],
    "windspeed" : [6,7,2],
    "event" : ["Rain" , "Sunny" , "Snow"]
}

print(weather_data)

data = pd.DataFrame(weather_data)
print(data.head(10))

print(data[["day" , "event"]])



weather_data1 = [
    ('1/1/2017' , 32  ,6 , "Rain"),
    ('1/2/2017' , 35 , 7 , 'Sunny')
]

data1 = pd.DataFrame(weather_data1 , columns=["day" , "temperature" , "windspeed" , "Event"])
print(data1.head())





