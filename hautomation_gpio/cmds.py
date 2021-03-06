from utils import *
import RPIO
from hautomation_gpio import WrongGPIOConfiguration, USED_GPIO_LIST

import logging

logger = logging.getLogger("driver")
try:
    from django.conf import settings
except:
    import hautomation_gpio.settings

logger.setLevel(settings.LOG_LEVEL)


def set_to_output(address):
    RPIO.setup(address, RPIO.OUT)


def pl_switch(address, value):
    if value not in ["on", "off"]:
        raise ValueError("Switch value must be 'on' or 'off'")
    address = int(address)
    validate_address(address)

    set_to_output(address)
    RPIO.output(address, value == "on")


def pl_all_lights_on():
    for pin in USED_GPIO_LIST:
        try:
            pl_switch(pin, "on")
        except WrongGPIOConfiguration:
            continue


def pl_all_lights_off():
    for pin in USED_GPIO_LIST:
        try:
            pl_switch(pin, "off")
        except WrongGPIOConfiguration:
            continue

