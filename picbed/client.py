import requests
import json
from PIL import ImageGrab, Image
import clipboard, pickle
import time, os
import json

class Client():
    """获取token"""
    def __init__(self):
        config=self.load('config.json')
        self.url = config["url"]
        self.username = config["username"]
        self.password = config["password"]
        print(self.url+self.username+self.password)
        self.headers = {'Content-Type': 'application/json'}
        self.payload = {'username':self.username, 'password':self.password}
        self.pkiFile = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'token.pki')
    
    def load(self,fname):
        filename=fname   #读取json文件中的某个数值
        with open(filename,encoding='utf-8') as f:
            pop_data=json.load(f)
            return pop_data
    
    def getToken(self):
        # 获取token
        token = {}
        r = requests.post(self.url,headers=self.headers, data=json.dumps(self.payload))
        t = r.text 
        timestamp = int(time.time())
        token.setdefault('token', t)
        token.setdefault('timestamp', timestamp)
        with open(self.pkiFile, 'wb') as f:
            pickle.dump(token,f)

    def showToken(self):
        # 从文件获取token
        with open(self.pkiFile, 'rb') as f:
            t = pickle.load(f)
            return t.get('token')

    def tokenExpired(self):
        # 验证是否过期
        if not os.path.exists(self.pkiFile):
            self.getToken()
        with open(self.pkiFile, 'rb') as f:
            token = pickle.load(f)
        if int(time.time()) - token.get('timestamp') > 600:
            return True
        else:
            return False


    def upload(self):
        upload_url = self.url + 'upload'
        #files = {'image001': open(r'001.jpg', 'rb')}
        files= {"image001":open(os.sep.join(['','001.jpg']), "rb")}
        h1 = {'token':token}
        ru = requests.post(upload_url, files=files)
        print(ru.text)

if __name__ == '__main__':
    c = Client()
    token = c.showToken()
    c.upload()
