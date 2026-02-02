import random
import time

sensor_data = []

for i in range(10):
    temperature = round(random.uniform(18.0, 30.0), 2)
    sensor_data.append(temperature)
    print(f"Reading {i+1}: {temperature} °C")
    time.sleep(1)

print("\nSummary:")
print(f"Average temperature: {sum(sensor_data)/len(sensor_data):.2f} °C")
print(f"Min temperature: {min(sensor_data)} °C")
print(f"Max temperature: {max(sensor_data)} °C")
