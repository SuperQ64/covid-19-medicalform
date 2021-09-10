import os
import json
import subprocess
import platform

def run_print(file_name):
    os_name = platform.system()
    if os_name == 'Windows':
        with open('./resource/property.json','r',encoding='utf-8') as f:
            prope = json.load(f)
            
        os.system('print.bat ' + file_name + ' ' + prope['printer'] + ' ' + prope['driver'] + ' ' + prope['port'])
    elif os_name == 'Linux':
        subprocess.run('sh ./print.sh ./out/' + file_name,shell=True)