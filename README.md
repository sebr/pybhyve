# 🚰 pybhyve: An async library for Orbit BHyve irrigation systems

`pybhyve` is a Python3, asyncio-driven library that interfaces with both the
REST and Websocket APIs provided by [Orbit BHyve](https://orbitbhyve.com/).

`pybhyve` is an unofficial API and is not endorsed by or supported by Orbit. The API
is not publicly documented and this library has been reverse engineered. As such,
there are no guarantees that it will continue to work.

If this code has been useful to you, please consider chipping in and buying me a coffee!

<a href="https://www.buymeacoffee.com/sebr" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee"></a>

Many thanks to [@bachya](https://github.com/bachya/) for laying most of the groundwork with [bachya/aioambient](https://github.com/bachya/aioambient/).

## Installation

```python
pip install pybhyve
```

### Python Versions

`pybhyve` is currently supported on:

- Python 3.6
- Python 3.7
- Python 3.8

## Usage

```python
import asyncio

from aiohttp import ClientSession

from pybhyve import Client

async def async_websocket_handler(data):
    _LOGGER.info("Websocket data: %s", data)

async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as session:
        client = Client("<YOUR USERNAME>", "<YOUR PASSWORD>", asyncio.get_event_loop(), session, async_websocket_handler)
        await client.login()

        # Get all devices in an account:
        devices = await client.devices

        _LOGGER.info("Devices: %s", devices)


asyncio.get_event_loop().run_until_complete(main())
```

## Contributing

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
