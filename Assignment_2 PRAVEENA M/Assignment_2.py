import requests
a= "https://api.openweathermap.org/data/2.5/weather?q=Chennai,IN&appid=5c3a4cc6799706c0ef54f8e06cdd1646"
r=requests.get(url=a)

data =r.json()
print (data)




tem =data['main'] ['temp']
print("temperature is :", tem)
hum =data['main'] ['humidity'] 
print ("humidity is :", hum)

temperature = 88
if temperature > 50:
         print("Temperature is High Alarm On")
else:
         print("Alarm OFF")








