# ONNX Operators and Activations Checker for Barracuda

![image](https://github.com/s4k10503/ONNX-Operators-and-Activations-Checker-for-Barracuda/assets/50241623/d934aa46-75aa-488b-b5c3-97e2d8292ab1)

## Overview

This application allows users to load ONNX models and automatically check for operators and activation functions that are not supported by Unity Barracuda.  
It is built using Python and leverages the customtkinter library for a modern and stylish GUI.

## Features

- Load ONNX Model: A user-friendly GUI button for loading ONNX files.
- Check Operators: Automatically scans the ONNX model to identify unsupported operators.
- Check Activation Functions: Automatically scans the ONNX model to identify unsupported activation functions.
- Progress Bar: Provides real-time feedback during the checking process.

## Dependencies

- Python 3.x
- ONNX
- customtkinter
- tkinter

## Running with Docker

To run this application using Docker, you can build and run a Docker container as follows:

### Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t onnx_checker .
```

### Run the Docker Container

Run the following command to run the Docker container.  
This also mounts the host directory to the container, enabling file access for the GUI.  

```bash
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /path/on/host:/path/in/container onnx_checker
```

Note: Replace /path/on/host and /path/in/container with the appropriate paths.

Security Note: Make sure to run xhost + on the host machine to allow connections to the X server:

```bash
xhost +
```

After you are done, restrict the X server access again with:

```bash
xhost -
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
