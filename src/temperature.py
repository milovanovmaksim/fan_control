from logging import debug
from typing import Union


class Temperature():
    """
    Температура CPU Raspberry Pi4.
    """
    def __init__(self, path: str) -> None:
        self._path = path

    def temperature(self) -> Union[int, ValueError]:
        """
        Определяет температуру CPU Raspberry pi4.
        """
        with open(self._path) as reader:
            try:
                temeperature = int(reader.readline())
                return round(temeperature / 1000)
            except ValueError as e:
                debug(f"Temperature.temperature | {e}")
                return e
