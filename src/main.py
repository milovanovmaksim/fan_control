import logging

import RPi.GPIO as GPIO

from src.control import FanControl
from src.fan import Fan
from src.temperature import Temperature


def main():
    temp_min = 40
    temp_max = 60
    delay = 2
    fan_pin = 18
    path = "/sys/class/thermal/thermal_zone0/temp"
    fan_low = 20
    fan_high = 100
    pwm_freq = 100
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(fan_pin, GPIO.OUT)
    fan_pwm = GPIO.PWM(fan_pin, pwm_freq)
    control = FanControl(Fan(Temperature(path), temp_min, temp_max, fan_low, fan_high, fan_pwm), delay)
    try:
        control.run()
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()

