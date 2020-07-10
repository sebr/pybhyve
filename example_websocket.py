"""Run an example script to quickly test."""
import asyncio
import logging

from aiohttp import ClientSession

from pybhyve import Client
from pybhyve.errors import WebsocketError

_LOGGER = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

USERNAME = "username"
PASSWORD = "password"


async def async_websocket_handler(data):
    _LOGGER.info("Websocket data %s", data)

async def main() -> None:
    """Run the websocket example."""

    async with ClientSession() as session:
        client = Client(USERNAME, PASSWORD, asyncio.get_event_loop(), session, async_websocket_handler)
        await client.login()

        for _ in range(30):
            _LOGGER.info("Waiting for messages...")
            await asyncio.sleep(5)

        await client.stop()


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
