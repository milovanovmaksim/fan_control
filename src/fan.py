from logging import debug, error
from typing import Union, TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from src.config import Config
    from RPi.GPIO import PWM
from src.temperature import Temperature


class Fan:
    """
    Вентилятор охлаждения Raspberry Pi.
    """
    def __init__(self, temperature: Temperature, config: "Config", pwm: "PWM"):
        self._temperature = temperature
        self.config = config
        self._pwm = pwm

    def start(self):
        debug("Fan.start | The fat is starting....")
        self._pwm.start(8)

    def _duty_cycle(self) -> Union[int, ValueError]:
        """

        """
        temperature = self._temperature.temperature()
        frequency = 0
        if isinstance(temperature, int):
            if temperature > self.config.temp_max:
                frequency = 100
            elif temperature > self.config.temp_min:
                frequency = round(((92 * (temperature - self.config.temp_min)) / (self.config.temp_max - self.config.temp_min)) + 8)
                if frequency > 100:
                    frequency = 100
            debug(f"Fan._duty_cycle | frequency = {frequency}, temperature = {temperature}")
            return frequency
        else:
            error(f"Fan._duty_cycle  | {temperature}")
            return temperature

    def update_fan_frequency(self) -> Optional[Exception]:
        duty_cycle = self._duty_cycle()
        if isinstance(duty_cycle, int):
            self._pwm.ChangeDutyCycle(duty_cycle)
        else:
            error(f"Fan.update_fan_frequency | {duty_cycle}")
            return duty_cycle
