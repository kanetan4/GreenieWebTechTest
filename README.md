# Power Consumption Estimation of Applications
This is a Python program that uses the psutil library to estimate the power consumption of applications on a computer.

## Requirements
Python 3.x
psutil library (version 5.8.0 or later)
You can install the psutil and matplotlib library using pip:

```pip install psutil```

```pip install matplotlib```

## Usage
1. Run the Python code.
2. Enter the names of the applications you want to compare. 
3. You can add up to two applications to compare. 
4. Enter "-1" to break.
5. The code will measure the power consumption of each application for a specified duration of 5 seconds.
6. The code will display a graph comparing the power consumption of each application.

Note: The current code may not measure power consumption of apps that are running in the background or not performing any activities.

## Functions
1. get_power_consumption(app_name) - returns the power consumption of a given application.
2. measure_power_consumption(app_names, duration) - measures the power consumption of a list of applications for a specified duration and displays the results as a graph.

## How it Works
The program uses psutil to find the process ID of the specified application and then estimates its power consumption based on its CPU usage and memory usage. The estimation is calculated as follows:

```power_consumption = cpu_percent * mem_info.rss / 1000  # mW```

Where cpu_percent is the CPU usage of the process as a percentage, and memory_usage is the memory usage of the process in bytes.

Note that this is just an estimation and may not be very accurate. The actual power consumption of the application may vary depending on the hardware and operating system being used.

## Example Code
2 Application Comparison

```Enter an app to compare (-1 to break): Google Chrome```

```Enter an app to compare (-1 to break): Spotify```

1 Application 

```Enter an app to compare (-1 to break): Google Chrome```

```Enter an app to compare (-1 to break): -1```
