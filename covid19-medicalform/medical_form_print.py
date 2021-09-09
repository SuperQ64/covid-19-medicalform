import os
import subprocess
import platform

def print(print_file):
    os_name = platform.system()
    if os_name == 'Windows':
        os.system('print.bat ' + print_file)
    elif os_name == 'Linux':
        subprocess.run('sudo ./print.sh ' + print_file,shell=True)