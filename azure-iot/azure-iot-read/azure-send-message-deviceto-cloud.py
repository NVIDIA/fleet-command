# Copyright (c) 2021 NVIDIA CORPORATION. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
import time
import datetime

async def main():
    # Fetch the connection string from an enviornment variable
    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
    hostname = os.getenv("HOSTNAME")

    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message to {}".format(conn_str))
    #tail = sh.tail("-f", "/home/deepstream.log", _iter=True)
    tail = os.popen("cat /home/deepstream.log | tail -125f | grep -v -e '^$'")
    #await device_client.send_message("This is a message that is being sent from {}".format(hostname))
    await device_client.send_message("{} host current time is {}".format(hostname, str(datetime.datetime.now())))
    await device_client.send_message(tail.read())
    #await device_client.send_message("This is a message that is being sent from {}".format(hostname))
    print("Message successfully sent!")
    print()

    # finally, disconnect
    await device_client.disconnect()


if __name__ == "__main__":
    while True:
        time.sleep(3)
        asyncio.run(main())
