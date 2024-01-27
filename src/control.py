from logging import debug
from src.fan import Fan
import time


class FanControl:
    """
    Контроль частоты вращения вентилятора от температура CPU.
    """
    def __init__(self, fan: Fan, delay: int):
        self._fan = fan
        self._delay = delay

    def run(self):
        debug("Control.run | Control is running...")
        while True:
            frequency = self._fan.update_fan_frequency()
            time.sleep(self._delay)
