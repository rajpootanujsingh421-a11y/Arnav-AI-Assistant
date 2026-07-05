import psutil

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)    
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")
    ram_percent = ram.percent
    disk_percent = disk.percent
    return f"""
    💻System Status
    
    CPU Usage : {cpu}%
    RAM Usage : {ram_percent}%
    Disk Usage : {disk_percent}%
    
    """