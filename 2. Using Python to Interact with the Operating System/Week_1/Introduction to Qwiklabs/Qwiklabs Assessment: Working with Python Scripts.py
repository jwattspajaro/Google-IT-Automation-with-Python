py#!/usr/bin/env python3
import shutil
import psutil
from network import *

def check_disk_usage(disk):
    """Verifica que haya suficiente espacio libre en el disco"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Verifica que haya suficiente CPU sin usar"""
    usage = psutil.cpu_percent(1)
    return usage < 75

# Si no hay suficiente espacio en el disco o suficiente CPU, imprime un error
if not check_disk_usage('/') or not check_cpu_usage():
    print("¡ERROR!")
elif check_localhost() and check_connectivity():
    print("Todo está bien")
else:
    print("Fallaron las comprobaciones de red")


