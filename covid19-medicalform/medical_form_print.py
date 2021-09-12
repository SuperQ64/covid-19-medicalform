import os
import json
import subprocess
import platform

acrobat_path = 'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'

def run_print(file_name):
    os_name = platform.system()
    with open('./resource/property.json','r',encoding='utf-8') as f:
        prope = json.load(f)
    if os_name == 'Windows':
        file_path = os.getcwd() + '/../download/' + file_name
        subprocess.run(['start' , '' , acrobat_path , '/t' , file_path , prope['printer'] , prope['driver'] , prope['port']] , shell=True)
        subprocess.run(['timeout' , '/t' , '10'] , shell=True)
        subprocess.run(['taskkill' , '/F' , '/IM' , 'AcroRd32.exe'])
    elif os_name == 'Linux':
        file_path = '../download/' + file_name
        subprocess.run(['lpr' , file_path] , shell=True)

if __name__ == '__main__':
    test_file = 'test.pdf'
    run_print(test_file)