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


def print_data(data):
    """Print data as it is received."""
    _LOGGER.info("Data received: %s", data)

def print_hello():
    """Print a simple "hello" message."""
    _LOGGER.info("Client has connected to the websocket")


async def main() -> None:
    """Run the websocket example."""

    async with ClientSession() as session:
        client = Client(USERNAME, PASSWORD, session)
        await client.api.login()

        try:
            ws = client.api.websocket
            ws.on_connect(print_hello)
            ws.on_message(print_data)
            await ws.connect()
        except WebsocketError as err:
            _LOGGER.error("There was a websocket error: %s", err)
            return

        for _ in range(30):
            _LOGGER.info("Waiting...")
            await asyncio.sleep(5)

        await client.api.websocket.disconnect()


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
