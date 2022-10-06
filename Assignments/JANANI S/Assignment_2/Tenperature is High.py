import time
import random
i=0
while(i<=1200):
 i=i+1
 time.sleep(6)
 temp=35
 humid=7
 if temp>=31:
    print(temp,"temperature is High and Alarm is On")
 elif temp<=20:
    print(temp,"temperature is normal")
 else:
    print(temp,"temperature is low")
 if humid<=7:
    print(humid,"humidity is Low")
 elif humid<=30:
    print(humid,"humidity is normal")
 else:
    print(humid,"humidity is High")
