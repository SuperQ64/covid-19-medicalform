import urllib.request
import urllib.error
import shutil

def file_download(url,save_name):
    try:
        file = urllib.request.urlopen(url).read()
        with open(save_name,mode='wb') as f:
            f.write(file)
        shutil.move('./' + save_name,'./download/')
    except urllib.error.URLError as e:
        print('QRコードを適切に読み込めませんでした。')
        return False
    except shutil.Error as e:
        print('このPDFは既に端末内に存在しています。削除した後、再ダウンロードします。')
        file_download(url,save_name)

    return True


            

if __name__ == '__main__':
    test_url = 'https://www.mhlw.go.jp/content/000782621.pdf'
    test_save_name = 'test.pdf'
    file_download(test_url,test_save_name)