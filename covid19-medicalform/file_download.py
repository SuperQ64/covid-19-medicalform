import urllib.request
import shutil

def file_download(url,save_name):
    file = urllib.request.urlopen(url).read()
    with open(save_name,mode='wb') as f:
        f.write(file)
    shutil.move('./' + save_name,'./download/')
            

if __name__ == '__main__':
    test_url = 'https://www.mhlw.go.jp/content/000782621.pdf'
    test_save_name = 'test.pdf'
    file_download(test_url,test_save_name)