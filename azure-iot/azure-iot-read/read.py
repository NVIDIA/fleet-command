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

import asyncio
from azure.eventhub import TransportType
from azure.eventhub.aio import EventHubConsumerClient
import os
import logging

# Event Hub-compatible endpoint
# az iot hub show --query properties.eventHubEndpoints.events.endpoint --name {your IoT Hub name}
EVENTHUB_COMPATIBLE_ENDPOINT = "{your Event Hubs compatible endpoint}"

# Event Hub-compatible name
# az iot hub show --query properties.eventHubEndpoints.events.path --name {your IoT Hub name}
EVENTHUB_COMPATIBLE_PATH = "{your Event Hubs compatible name}"

# Primary key for the "service" policy to read messages
# az iot hub policy show --name service --query primaryKey --hub-name {your IoT Hub name}
IOTHUB_SAS_KEY = "{your service primary key}"

# If you have access to the Event Hub-compatible connection string from the Azure portal, then
# you can skip the Azure CLI commands above, and assign the connection string directly here.
#CONNECTION_STR = f'Endpoint={EVENTHUB_COMPATIBLE_ENDPOINT}/;SharedAccessKeyName=service;SharedAccessKey={IOTHUB_SAS_KEY};EntityPath={EVENTHUB_COMPATIBLE_PATH}'
CONNECTION_STR = os.getenv("IOTHUB_CONNECTION_STRING") 

# Define callbacks to process events
async def on_event_batch(partition_context, events):
    for event in events:
        #print("Received event from partition: {}.".format(partition_context.partition_id))
        print("Telemetry received: ", event.body_as_str())
       #print("Properties (set by device): ", event.properties)
        #print("System properties (set by IoT Hub): ", event.system_properties)
        print()
    await partition_context.update_checkpoint()

async def on_error(partition_context, error):
    # Put your code here. partition_context can be None in the on_error callback.
    if partition_context:
        print("An exception: {} occurred during receiving from Partition: {}.".format(
            partition_context.partition_id,
            error
        ))
    else:
        print("An exception: {} occurred during the load balance process.".format(error))


async def main():
    loop = asyncio.get_event_loop()
    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        consumer_group="$default",
        eventhub_name = os.getenv("IOTHUB_NAME")
        #eventhub_name="egx-iot"
        # transport_type=TransportType.AmqpOverWebsocket,  # uncomment it if you want to use web socket
        # http_proxy={  # uncomment if you want to use proxy 
        #     'proxy_hostname': '127.0.0.1',  # proxy hostname.
        #     'proxy_port': 3128,  # proxy port.
        #     'username': '<proxy user name>',
        #     'password': '<proxy password>'
        # }
    )
    try:
        #print("try loop")
        recv_task = asyncio.ensure_future(client.receive_batch(on_event_batch=on_event_batch, on_error=on_error))
        #loop.run_until_complete(client.receive_batch(on_event_batch=on_event_batch, on_error=on_error))
        await asyncio.sleep(3)
        recv_task.cancel()
        await client.close()
    except KeyboardInterrupt:
        print("Receiving has stopped.")
   
if __name__ == '__main__':
    while True:
        asyncio.run(main())
