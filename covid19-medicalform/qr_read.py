import json
import medical_form as mf
import medical_form_print as mfp

def main():
    while True:
        print('please input QRcode')
        url = input()   #https://****/{接種券番号}
        url.replace('+',':')
        div_url = url.split('/')
        id = div_url[len(div_url) - 1]
        file_out = './out/' + id + '.pdf'

        if id == 'end':
            break

        with open('./resource/template_v2.json',"r",encoding="utf-8") as f:
            # 予診票に書き込む情報を読み込む
            json_file = json.load(f)

        info = json_file[id]


        mf.write(info=info,file_out=file_out)

        mfp.print(print_file=file_out)

    
    print('entered [end]')

if __name__ == '__main__':
    main()

