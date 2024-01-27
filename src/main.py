import logging

from src.control import FanControl
from src.fan import Fan
from src.temperature import Temperature


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.ERROR)
    temp_min = 40
    temp_max = 80
    delay = 3
    pin = 14
    path = "/sys/class/thermal/thermal_zone0/temp"
    control = FanControl(
        Fan(Temperature(path), temp_min, temp_max, pin),
        delay)
    control.run()


if __name__ == "__main__":
    main()
