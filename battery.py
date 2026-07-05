import psutil

def get_battery():
    battery = psutil.sensors_battery()  
    percent = battery.percent
    charging = battery.power_plugged
    if charging:
        status = "Charging ⚡"
    else:
        status = "Not Charging 🔋"
        
    return f"Battery: {percent}%\nStatus: {status}"
