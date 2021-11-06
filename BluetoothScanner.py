# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to test Bluetooth functionality


import asyncio
from bleak import BleakScanner
from bleak import BleakClient


async def scan_bt_devices():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(scan_bt_devices())
