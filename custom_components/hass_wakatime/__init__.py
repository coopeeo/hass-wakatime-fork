"""Display your Wakatime stats in Home Assistant."""

from typing import TYPE_CHECKING
from logging import getLogger

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant


DOMAIN = "hass_wakatime"

LOGGER = getLogger(__name__)


async def async_setup(hass: "HomeAssistant", config):
    LOGGER.debug("hass_wakatime loaded with config %r", (config))
    # LOGGER.debug("loaded", config)
    return True
