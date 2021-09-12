import qr_read as q
import file_download as fd
import medical_form_print as mfp

def main():
    while True:
        qr_string = q.qr_read()
        file_name = ''
        fd.file_download(url=qr_string,save_name=file_name)
        mfp.run_print(file_name=file_name)

if __name__ == '__main__':
    main()