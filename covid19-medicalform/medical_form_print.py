import os
import json
import subprocess
import platform

def run_print(file_name):
    os_name = platform.system()
    with open('./resource/property.json','r',encoding='utf-8') as f:
        prope = json.load(f)
    if os_name == 'Windows':
        os.system('print.bat ' + file_name + ' ' + prope['printer'] + ' ' + prope['driver'] + ' ' + prope['port'])
    elif os_name == 'Linux':
        subprocess.run('sh ./print.sh ./out/' + file_name + ' ' + prope['printer'],shell=True)