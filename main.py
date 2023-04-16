import psutil
import matplotlib.pyplot as plt

def get_power_consumption(app_name):
    # Get the process ID of the application
    pid = None
    for p in psutil.process_iter(['pid', 'name'],1):
        if app_name.lower() in p.info['name'].lower():
            pid = p.info['pid']
            break

    if pid is None:
        print(f"No process found with the name '{app_name}'.")
        return None
    else:
        # Get the power consumption of the application
        process = psutil.Process(pid)
        cpu_percent = process.cpu_percent(interval=1)
        mem_info = process.memory_info()
        power_consumption = cpu_percent * mem_info.rss / 1000  # mW
        return power_consumption

# User input of applications to compare
choice = ""
app_list = []
while choice != "-1":
    choice = input("Enter an app to compare (-1 to break): ")
    if choice == "-1":
        break
    else:
        app_list.append(choice)
    

# app_list = ["Google Chrome", "Microsoft Word", "Notion"]

# Get the power consumption of each application
power_consumptions = []
for app in app_list:
    power_consumption = get_power_consumption(app)
    if power_consumption is not None:
        power_consumptions.append(power_consumption)

# Plot a bar chart of the power consumption of each application
fig, ax = plt.subplots()
bars = ax.bar(range(len(app_list)), power_consumptions)
ax.set_xticks(range(len(app_list)))
ax.set_xticklabels(app_list)
ax.set_ylabel("Power Consumption (mW)")
ax.set_title("Power Consumption of Applications")

# Add the exact values of power consumption on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.2f}", ha='center', va='bottom')

plt.show()
