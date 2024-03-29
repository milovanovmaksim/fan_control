from logging import error
from typing import Union


class Temperature():
    """
    Температура CPU Raspberry Pi4.
    Params:
        path - путь к файлу с которогу можно прочитать температуру процессоора.
        Для Raspberry Pi /sys/class/thermal/thermal_zone0/temp.
    """
    def __init__(self, path: str):
        self._path = path

    def temperature(self) -> Union[int, Exception]:
        """
        Читает температуру CPU Raspberry pi4 из файла.
        """
        try:
            with open(self._path, "r") as reader:
                try:
                    temeperature = int(reader.readline())
                    return round(temeperature / 1000)
                except ValueError as e:
                    error(f"Temperature.temperature | {e}")
                    return e
        except Exception as e:
            error(f"Temperature.temperature | {e}")
            return e
