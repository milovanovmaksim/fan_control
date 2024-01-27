from logging import debug, error
from typing import Union

from src.temperature import Temperature


class Fan:
    """
    Вентилятор охлаждения Raspberry Pi.
    """
    def __init__(self, temperature: Temperature, temp_min: int, temp_max: int, pin: int):
        self._temperature = temperature
        self._temp_max = temp_max
        self._temp_min = temp_min
        self._pin = pin

    def frequency(self) -> Union[int, ValueError]:
        """
        Определяет частоту вращения вентилятора охлаждения в зависимости от температуры CPU Raspberry Pi4.
        """
        temperature = self._temperature.temperature()
        frequency = 0
        if isinstance(temperature, int):
            if temperature > self._temp_max:
                frequency = 100
            elif temperature > self._temp_min:
                frequency = round((100 * (temperature - self._temp_min)) / (self._temp_max - self._temp_min))
            debug(f"Fan.frequency | frequency = {frequency}, temperature = {temperature}")
            return frequency
        else:
            error("main | {}", temperature)
            return temperature
