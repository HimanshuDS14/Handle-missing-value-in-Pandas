import pandas as pd
import numpy as np

data = pd.read_csv("weather_data1.csv" , parse_dates=["day"] , index_col='day')

print(data.head())


new_data = data.fillna(0)
print(new_data.head())

new_data = data.fillna({
    "temperature" : 0,
    "windspeed" : 0,
    "event" : "no event"
})
print(new_data)

#other way fill value

new_data = data.fillna(method="ffill")
print(new_data)

new_data = data.fillna(method="bfill")
print(new_data)

new_data = data.interpolate()
print(new_data)

new_data = data.dropna()
print(new_data)


new_data = data.replace(np.nan , -99999)
print(new_data)

new_data = data.replace( np.nan , {
    "temperature" : 0,
    "windspeed" : 0.0,
    "event" : "No event"
})
print(new_data)





