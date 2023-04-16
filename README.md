# Power Consumption Estimation of a Single Application
This is a Python program that uses the psutil library to estimate the power consumption of a single application on a computer.

## Requirements
Python 3.x
psutil library (version 5.8.0 or later)
You can install the psutil library using pip:

```pip install psutil```

## Usage
Open a command prompt or terminal.
Navigate to the directory where the power_consumption.py file is located.
Run the command python power_consumption.py your_application_name, where your_application_name is the name of the application you want to measure the power consumption of.
For example, to measure the power consumption of Google Chrome, you can run:

```python power_consumption.py chrome```

## How it Works
The program uses psutil to find the process ID of the specified application and then estimates its power consumption based on its CPU usage and memory usage. The estimation is calculated as follows:

```power_consumption = cpu_percent * memory_usage / 1000  # mW```

Where cpu_percent is the CPU usage of the process as a percentage, and memory_usage is the memory usage of the process in bytes.

Note that this is just an estimation and may not be very accurate. The actual power consumption of the application may vary depending on the hardware and operating system being used.

## License
This program is licensed under the MIT License. See the LICENSE file for details.
