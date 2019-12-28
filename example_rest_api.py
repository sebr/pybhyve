"""Run an example script to quickly test."""
import asyncio
import logging

from aiohttp import ClientSession

from pybhyve import Client
from pybhyve.errors import BHyveError

_LOGGER = logging.getLogger()

USERNAME = "username"
PASSWORD = "password"

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.INFO)
    async with ClientSession() as session:
        try:
            client = Client(USERNAME, PASSWORD, session)
            await client.api.login()

            devices = await client.api.devices
            _LOGGER.info("Devices: %s", devices)

        except BHyveError as err:
            _LOGGER.error("There was an error: %s", err)


asyncio.get_event_loop().run_until_complete(main())
