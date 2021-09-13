import sys
import platform

def qr_read():
    print('QRコードをかざしてください')
    url = input()
    if url == 'end':
        print('プログラムを終了します')
        sys.exit()
    if platform.system() == 'Windows':
        url = replace_url(url)

    div_url = url.split('/')
    id = ''
    password = ''
    request_url = ''

    return request_url

def replace_url(url):
    list = [['+',':'],['^','='],['\'','&']]
    fixed_url = url
    for pair in list:
        fixed_url = fixed_url.replace(pair[0],pair[1])

    return fixed_url


if __name__ == '__main__':
    request_url = qr_read()
    print(request_url)