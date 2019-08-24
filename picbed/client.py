import requests
import os

def upload():
    upload_url = 'http://127.0.0.1:10000/upload'
    files= {"image001":open('1.png', "rb")}
    ru = requests.post(upload_url, files=files)
    print(ru.text)

if __name__ == '__main__':
    upload()
