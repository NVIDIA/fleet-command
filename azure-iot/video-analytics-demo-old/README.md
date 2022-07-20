## What is the Intelligent Video Analytics ?

- Easy to use demo to demonstrate GPU accelerated Inference

- Based on the NGC Deepstream Container (https://ngc.nvidia.com/catalog/containers/nvidia:deepstream)

- Leverages Kubernetes, Helm, NGC, DeepStream

- Best deployed via Helm to deploy the application

- Does not require a Video Management System (VMS)

## What is DeepStream?

DeepStream SDK delivers a complete streaming analytics toolkit for real-time AI based video and image understanding and multi-sensor processing. DeepStream SDK features hardware-accelerated building blocks, called plugins that bring deep neural networks and other complex processing tasks into a stream processing pipeline. The SDK allows you to focus on building core deep learning networks and IP rather than designing end-to-end solutions from scratch.

More information on the DeepStream container here: (https://ngc.nvidia.com/catalog/containers/nvidia:deepstream)

### Running the Video Analytics Demo 

#### Prerequisites
- Kubernetes Cluster
- Helm/Tiller
- NVIDIA GPU Operator
- Run the helm chart

Execute the below commands to deploy the Intelligent Video Analytics Demo with built-in Video and WebUI

```
helm fetch https://helm.ngc.nvidia.com/nvidia/charts/video-analytics-demo-0.1.5.tgz

helm install video-analytics-demo-0.1.5.tgz
```

If you want to use camera as input, Please follow the below steps to deploy Intelligent Video Analytics Demo.

```
1. helm fetch https://helm.ngc.nvidia.com/nvidia/charts/video-analytics-demo-0.1.5.tgz --untar

2. cd into the folder video-analytics-demo and update the file values.yaml

3. Go to the section Cameras in the values.yaml file and add the address of your IP camera. Read the comments section on how it can be added. Single or multiple cameras can be added as shown below
cameras:
 camera1: rtsp://XXXX
 camera2: rtsp://XXXX

4. helm install video-analytics-demo
```

View the infered RTSP feed

1. Use the below WebUI URL to access deepstream application from browser

```
http://IPAddress of Node:31115/WebRTCApp/play.html?name=videoanalytics
```

2. Download VLC Player from: https://www.videolan.org/vlc/ on the client machine where the user intends to view the video stream.We can view the video stream by entering the following URL in the VLC player.
```
rtsp://IPAddress of Node:31113/ds-test
```
IPAddress of the node can be viewed by executing ifconfig on the server node


## License
The DeepStream SDK license is available within the container at the location opt/nvidia/deepstream/deepstream-5.0/LicenseAgreement.pdf. By pulling and using the DeepStream SDK (deepstream) container in NGC, you accept the terms and conditions of this license.

## Suggested Reading
For more information on DeepStream documentation containing Development guide, Plug-ins manual, API reference manual, migration guide, FAQ and release notes can be found here https://docs.nvidia.com/metropolis/index.html

If you have any questions or feedback, please refer to the discussions on DeepStream SDK Forum.

For more information, including blogs and webinars, see the DeepStream SDK website

## Technical Support
Email: EGXSupport@nvidia.com
