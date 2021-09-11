import json
import medical_form as mf
import medical_form_print as mfp
import platform

def main():
    while True:
        print('QRコードをかざしてください')
        url = input()   #https://****/{接種券番号}
        if platform.system() == 'Windows':
            url = replace_url(url)
        div_url = url.split('/')
        id = div_url[len(div_url) - 1]
        file_name = id + '.pdf'

        if id == 'end':
            break

        with open('./resource/template_v2.json',"r",encoding="utf-8") as f:
            # 予診票に書き込む情報を読み込む
            json_file = json.load(f)

        info = json_file[id]
        mf.write(info=info,file_out='./out/' + file_name)
        mfp.run_print(file_name=file_name)
    
    print('終了します')

def replace_url(url):
    list = [['+',':'],['=','_']]
    fixed_url = url
    for pair in list:
        fixed_url = fixed_url.replace(pair[0],pair[1])

    return fixed_url

if __name__ == '__main__':
    main()

