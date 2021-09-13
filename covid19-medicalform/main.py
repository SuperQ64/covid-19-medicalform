import sys
import json
import medical_form as mf
import qr_read as qr
import file_download as fd
import medical_form_print as mfp

def main():
    while True:
        qr_string = qr.qr_read()
        file_name = ''
        fd.file_download(url=qr_string,save_name=file_name)
        mfp.run_print(file_name=file_name)

def test():
    while True:
        print('QRコードをかざしてください。')
        qr_string = input()
        if qr_string == 'end':
            sys.exit()
        id = ''
        with open('./resource/template_v2.json',mode='r',encoding='utf-8') as f:
            json_info = json.load(f)

        info = json_info[id]
        mf.write(info=info,file_out='./out/' + id + '.pdf')
        mfp.test_run_print(file_name=id + '.pdf')

if __name__ == '__main__':
    test()