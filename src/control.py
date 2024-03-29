from logging import debug, error
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.fan import Fan


class FanControl:
    """
    Контроль частоты вращения вентилятора от температура CPU.
    """
    def __init__(self, fan: "Fan", delay: int):
        self._fan = fan
        self._delay = delay

    def run(self):
        debug("Control.run | Control is running...")
        self._fan.start()
        while True:
            result = self._fan.update_fan_frequency()
            if isinstance(result, Exception):
                error(f"FanControl.run  | {result}")
                raise result
            time.sleep(self._delay)

    def stop(self):
        self._fan.stop()
