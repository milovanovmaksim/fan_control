from logging import debug, error
from typing import Union, TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from RPi.GPIO import PWM
    from src.temperature import Temperature


class Fan:
    """
    Вентилятор охлаждения Raspberry Pi.
    Params:
        temp_min - минимальная температура CPU при которой включается вентилятор охлаждения,
        temp_max - максимальная температура CPU при которой вентилятор охлаждения выходит на 100% частоту вращения,
        fan_low - минимальная скаважность ШИМ,
        fan_high - максимальная скважность ШИМб
        fan_pwm  - обект PWM.
    """
    def __init__(self, temperature: "Temperature", temp_min: int, temp_max: int, fan_low: int, fan_high: int, fan_pwm: "PWM"):
        self._temperature = temperature
        self._temp_min = temp_min
        self._temp_max = temp_max
        self._fan_low = fan_low
        self._fan_high = fan_high
        self._fan_pwm = fan_pwm

    def start(self):
        """
        Старт вентилятора на минимальной скважности.
        """
        debug("Fan.start | The fat is starting....")
        self._fan_pwm.start(self._fan_low)

    def _duty_cycle(self) -> Union[int, Exception]:
        """
        Определяет скважность ШИМ в зависимости от текущей температуры CPU.

        """
        temperature = self._temperature.temperature()
        frequency = 0
        if isinstance(temperature, Exception):
            error(f"Fan._duty_cycle  | {temperature}")
            return temperature
        else:
            if temperature > self._temp_max:
                frequency = 100
            elif temperature > self._temp_min:
                delta = self._fan_high - self._fan_low
                frequency = round(delta * (temperature - self._temp_min) / (self._temp_max - self._temp_min) + self._fan_low)
                if frequency > 100:
                    frequency = 100
            debug(f"Fan._duty_cycle | frequency = {frequency}, temperature = {temperature}")
            return frequency

    def update_fan_frequency(self) -> Optional[Exception]:
        """
        Обновляет скважность ШИМ для вентилятор.
        """
        duty_cycle = self._duty_cycle()
        if isinstance(duty_cycle, Exception):
            error(f"Fan.update_fan_frequency | {duty_cycle}")
            return duty_cycle
        else:
            self._fan_pwm.ChangeDutyCycle(duty_cycle)

    def stop(self):
        self._fan_pwm.stop()
