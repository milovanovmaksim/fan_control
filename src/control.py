from logging import debug
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.config import Config

from src.fan import Fan


class FanControl:
    """
    Контроль частоты вращения вентилятора от температура CPU.
    """
    def __init__(self, fan: Fan, config: "Config"):
        self._fan = fan
        self._config = config

    def run(self):
        debug("Control.run | Control is running...")
        self._fan.start()
        while True:
            self._fan.update_fan_frequency()
            time.sleep(self._config.delay)
