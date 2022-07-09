import time
import board
import adafruit_bmp280

i2c = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Calibrate the sensor
sensor.sea_level_pressure = 1011.85

while True:
    print(f"Temperature: {((sensor.temperature*1.8)+32):.2f} F")
    print(f"Pressure   : {(sensor.pressure / 33.86):.2f} in Hg")
    print(f"Altitude   : {(sensor.altitude * 3.3):.1f} ft MSL\n")
    time.sleep(5)
