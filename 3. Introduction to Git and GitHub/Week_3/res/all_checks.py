#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
    """Devuelve True si la computadora tiene un reinicio pendiente."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Devuelve True si hay suficiente espacio libre en el disco, False en caso contrario."""
    # Obtiene el uso del disco
    du = shutil.disk_usage(disk)
    # Calcula el porcentaje de espacio libre
    percent_free = 100 * du.free / du.total
    # Calcula cuántos gigabytes libres hay
    gigabytes_free = du.free / 2**30
    if percent_free < min_gb or gigabytes_free < min_percent:
        return False
    return True

def check_root_full():
    """Devuelve True si la partición raíz está llena, False en caso contrario."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    # Lista de comprobaciones a realizar, con su función correspondiente y el mensaje asociado
    checks = [(check_reboot, "Reinicio pendiente"), (check_root_full, "Partición raíz llena")]
    everything_ok = True
    # Itera sobre cada comprobación y su mensaje asociado
    for check, msg in checks:
        # Si la comprobación falla, imprime el mensaje asociado y marca que no todo está bien
        if check():
            print(msg)
            everything_ok = False

    # Si no todo está bien, sal del programa con un código de error
    if not everything_ok:
        sys.exit(1)

    # Si todo está bien, imprime un mensaje indicando que todo está bien y sal del programa con un código de éxito
    print("Todo está bien.")
    sys.exit(0)

# Llama a la función main al ejecutar el script
main()
