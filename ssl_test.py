import ssl
import certifi
import aiohttp

ssl_context = ssl.create_default_context(cafile=certifi.where())

session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context))
