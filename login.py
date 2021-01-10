import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from lxml import etree

from config import *

import requests


def login(account, password):
    # 密码进行加密处理
    password = '__RSA__' + encrypt(password)

    user = requests.session()
    user.headers.update({'User-Agent': userAgent})
    getResult = user.get('https://uis.nwpu.edu.cn/cas/login')
    form_data_execution = str(etree.HTML(getResult.content).xpath('//input[@name="execution"]/@value')[0])
    header = {
        'origin': 'https://uis.nwpu.edu.cn',
        'referer': 'https://uis.nwpu.edu.cn/cas/login',
    }
    postData = {
        'username': account,
        'password': password,
        'currentMenu': 1,
        'execution': form_data_execution,
        '_eventId': 'submit',
        'geolocation': '',
        'submit': 'One moment please...'
    }
    login_result = user.post('https://uis.nwpu.edu.cn/cas/login', data=postData,
                             headers=header)

    if login_result.status_code == 500:
        print("login error:response HTTP 500")
        exit(0)

    cookie = user.cookies
    if "TGC" in dict(cookie).keys() and (login_result.text.find('欢迎使用') != -1):
        user.get("http://yqtb.nwpu.edu.cn/")
        print(dict(user.cookies)['JSESSIONID'])
        return user
    else:
        print("login error @ login.py 46")
        exit(0)


def encrypt(content):
    content = bytes(content, "utf8")
    keyContent = requests.get("https://uis.nwpu.edu.cn/cas/jwt/publicKey").content
    pubKey = RSA.import_key(keyContent)
    cipherRSA = PKCS1_v1_5.new(pubKey)
    cipherText = base64.b64encode(cipherRSA.encrypt(content))
    return cipherText.decode('utf-8')
