import logging

import RPi.GPIO as GPIO

from src.control import FanControl
from src.fan import Fan
from src.temperature import Temperature
from src.config import Config


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.ERROR)
    config = Config()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(config.fan_pin, GPIO.OUT)
    fan_pwm = GPIO.PWM(config.fan_pin, 100)
    control = FanControl(
        Fan(Temperature(config), config, fan_pwm),
        config)
    try:
        control.run()
    except Exception:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
