# Video Analytics Demo with Azure IoT Integration

This repository helps you to test Deepstream Sample Application with Azure IoT on Fleet Command Edge Node. 

## Prerequisites 
- Access to Azure Account with an access to create Azure IoT Hub resources.
  - [Azure IoT Hub Event Connection String](https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/#eventhubconn)
  - [Azure IoT Device Connection String](https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/#iothubdeviceconn)

## Azure IoT Preparation

Create an Azure IoT resources, for more information please refer [Azure IoT Preparation](https://docs.google.com/document/d/1BZhJJr4oGKi2gVF4aAKY4I_nF-P3ParB-hxaH7pRIDE/edit#heading=h.dl1a8tw0t31x)

`NOTE:` Here Primary Connection string means Azure IoT Device Connection String

## Sample Application Preparation

Deepstream Intelligent Video Analytics Demo helm chart running Azure IoT as a sidecar and sending the Deepstream logs as a telemetry data to Azure IoT Hub. 

Provide the Azure IoT Device Connection string in values.yaml as per below 

```
iotdevice-connection-string: "HostName=egx-iot.azure-devices.net;DeviceId=egx-iot-device;SharedAccessKey=F1/EOVGtm2b3fFzXXxxXXaaXXXxXaaaXaXxxAxAa" 

```

## Deploy on Fleet Command

Please go through [Deploy to the Edge](https://docs.google.com/document/d/1ahm2WdTg0Z7T5to8HdXZho_gnyheGIDtxBB-QSEJHN8/edit#heading=h.mhpzm8t8vdmp) steps to deploy the Azure IoT Application on Fleet Command Edge Node using Fleet Command.

## Read the Azure IoT Telemetry Data

### Prerequisites
- Python3.7

Follow the below steps on your local machine to read the Azure IoT telemetry. 

Run below commands to install Azure IoT dependencies 

```
cd azure-iot-read
pip3 install -r requirements.txt
```

Now export the Azure IoT Hub Event connection string 
```
export IOTHUB_CONNECTION_STRING="Endpoint=sb://iothub-ns-egx-iot-5151100-ce38d2b8ec.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=ixAxsaXwaXaasfXxaxaaXads;EntityPath=egx-iot" 
```

Run the below command to read the telemetry of Azure IoT Hub

```
python3 read.py
```

# Azure IoT Runtime 

Deploy Azure IoT Runtime Helm Chart to connect Azure IoT

When you deploying, please provide Azure IoT edge device connection string as per below 

```
provisioning:
  deviceConnectionString: "HostName=egx-iot.azure-devices.net;DeviceId=fc-node;SharedAccessKey=EOVGtm2b3fFzXXxxXXaaXXXxXaaaXaXxxAxAa="
```
