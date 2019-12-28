# 🚰 pybhyve: An async library for Orbit BHyve irrigation systems

`pybhyve` is a Python3, asyncio-driven library that interfaces with both the
REST and Websocket APIs provided by [Orbit BHyve](https://orbitbhyve.com/).

`pybhyve` is an unofficial API and is not endorsed by or supported by Orbit. The API
is not publicly documented and this library has been reverse engineered. As such,
there are no guarantees that it will continue to work.

Many thanks to @bachya for laying most of the groundwork with bachya/aioambient

# Installation

```python
pip install pybhyve
```

# Python Versions

`pybhyve` is currently supported on:

- Python 3.6
- Python 3.7
- Python 3.8

# Usage

## Creating a Client

An `pybhyve` client starts with an
[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:

```python
import asyncio

from aiohttp import ClientSession

from pybhyve import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        # YOUR CODE HERE


asyncio.get_event_loop().run_until_complete(main())
```

Create a client, initialize it, then get to it:

```python
import asyncio

from aiohttp import ClientSession

from pybhyve import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        client = Client("<YOUR USERNAME>", "<YOUR PASSWORD>", websession)
        await client.api.login()

        # Get all devices in an account:
        await client.api.devices


asyncio.get_event_loop().run_until_complete(main())
```

## REST API

```python
import asyncio

from aiohttp import ClientSession

from pybhyve import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        client = Client("<YOUR USERNAME>", "<YOUR PASSWORD>", websession)
        await client.api.login()

        # Get all devices in an account:
        await client.api.devices


asyncio.get_event_loop().run_until_complete(main())
```

## Websocket API

```python
import asyncio

from aiohttp import ClientSession

from pybhyve import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        client = Client("<YOUR USERNAME>", "<YOUR PASSWORD>", websession)
        await client.api.login()

        # Define a method that should be fired when the websocket client
        # connects:
        def connect_method():
            """Print a simple "hello" message."""
            print("Client has connected to the websocket")

        client.api.websocket.on_connect(connect_method)

        # Define a method that should be run upon receiving data:
        def data_method(data):
            """Print the data received."""
            print(f"Data received: {data}")

        client.api.websocket.on_message(data_method)

        # Define a method that should be run when the websocket client
        # disconnects:
        def disconnect_method(data):
            """Print a simple "goodbye" message."""
            print("Client has disconnected from the websocket")

        client.api.websocket.on_disconnect(disconnect_method)

        # Connect to the websocket:
        await client.api.websocket.connect()

        # At any point, disconnect from the websocket:
        await client.api.websocket.disconnect()


loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
```

# Contributing

1. [Check for open features/bugs](https://github.com/sebr/pybhyve/issues)
   or [initiate a discussion on one](https://github.com/sebr/pybhyve/issues/new).
2. [Fork the repository](https://github.com/sebr/pybhyve/fork).
3. Install the dev environment: `make init`.
4. Enter the virtual environment: `source ./venv/bin/activate`
5. Code your new feature or bug fix.
6. Write a test that covers your new functionality.
7. Run tests and ensure 100% code coverage: `make coverage`
8. Update `README.md` with any new documentation.
9. Add yourself to `AUTHORS.md`.
10. Submit a pull request!
