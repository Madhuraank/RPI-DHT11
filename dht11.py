mport subprocess
import time
#subprocess.call("sudo pigpiod", shell=True)
#time.sleep(0.1)
from pigpio_dht import DHT11, DHT22
while True:
        gpio = 4 # BCM Numbering

        sensor = DHT11(gpio)
#sensor = DHT22(gpio)

        result = sensor.read()
        print(result)

        temperature=([value for value in result.values()][0])
        print(temperature)

        humidity=([value for value in result.values()][2])
        print(humidity)
        time.sleep(10)

