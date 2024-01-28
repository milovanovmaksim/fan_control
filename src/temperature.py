from logging import debug
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from src.config import Config


class Temperature():
    """
    Температура CPU Raspberry Pi4.
    """
    def __init__(self, config: "Config") -> None:
        self._config = config

    def temperature(self) -> Union[int, ValueError]:
        """
        Определяет температуру CPU Raspberry pi4.
        """
        with open(self._config.path) as reader:
            try:
                temeperature = int(reader.readline())
                return round(temeperature / 1000)
            except ValueError as e:
                debug(f"Temperature.temperature | {e}")
                return e
