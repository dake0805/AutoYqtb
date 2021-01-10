import re
import time

import pymysql
import requests
from lxml import etree
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

# mysql config
mysql_username = ""
mysql_passwd = ""
mysql_host = "101.132.227.83"


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
    user.post('https://uis.nwpu.edu.cn/cas/login', data=postData,
              headers=header)
    cookie = user.cookies
    if "TGC" in dict(cookie).keys():
        user.get("http://yqtb.nwpu.edu.cn/")
        print(dict(user.cookies)['JSESSIONID'])
        return user
    else:
        print("login error")
        exit(0)


def encrypt(content):
    content = bytes(content, "utf8")
    keyContent = requests.get("https://uis.nwpu.edu.cn/cas/jwt/publicKey").content
    pubKey = RSA.import_key(keyContent)
    cipherRSA = PKCS1_v1_5.new(pubKey)
    cipherText = base64.b64encode(cipherRSA.encrypt(content))
    return cipherText.decode('utf-8')


def yqtb(user, account, location, zip, hubei, name, xueyuan, cellphone, inschool, fxzt):
    if (fxzt == 1 & hubei == 1):
        print("error")
        exit(0)

    if (inschool == 1):
        zip = '1'
        location = '在学校'

    print(account + " " + location + " " + zip + " " + name + " " + xueyuan + " " + cellphone + " " + "fxzt" + fxzt)

    if (hubei == 1):
        data = {
            'sfczbcqca': '',
            'czbcqcasjd': '',
            'sfczbcfhyy': '',
            'czbcfhyysjd': '',
            'actionType': 'addRbxx',
            'userLoginId': account,
            'fxzt': fxzt,
            'userType': 2,
            'userName': name,
            'szcsbm': zip,  # 所在城市 2：在西安 3：其他
            'szcsmc': location,  # 所在城市名称
            'sfjt': '1',  # 是否经停
            'sfjtsm': '人在湖北',  # 是否经停说明
            'sfjcry': '1',  # 是否接触人员
            'sfjcrysm': '人在湖北',  # 是否接触人员说明
            'sfjcqz': '0',  # 是否接触确诊
            'sfyzz': '0',  # var sfyzz =  $('input[name='radio5']:checked').val();
            'sfqz': '0',  # 是否确诊
            'ycqksm': '',  # 异常情况说明
            'glqk': '0',  # 隔离情况
            'glksrq': '',  # 隔离开始日期
            'gljsrq': '',  # 隔离结束日期
            'tbly': 'sso',  # what's this?
            'glyy': '',  # 隔离原因
            'qtqksm': '',
            'sfjcqzsm': '',  # 是否接触确诊说明
            'sfjkqk': '0',
            'jkqksm': '',
            'sfmtbg': '',
            'qrlxzt': '',
            'xymc': xueyuan,
            'xssjhm': cellphone
        }
    else:
        data = {
            'sfczbcqca': '',
            'czbcqcasjd': '',
            'sfczbcfhyy': '',
            'czbcfhyysjd': '',
            'actionType': 'addRbxx',
            'userLoginId': account,
            'fxzt': fxzt,
            'userType': 2,
            'userName': name,
            'szcsbm': zip,  # 所在城市 2：在西安 3：其他
            'szcsmc': location,  # 所在城市名称
            'sfjt': '0',  # 是否经停
            'sfjtsm': '',  # 是否经停说明
            'sfjcry': '0',  # 是否接触人员
            'sfjcrysm': '',  # 是否接触人员说明
            'sfjcqz': '0',  # 是否接触确诊
            'sfyzz': '0',  # var sfyzz =  $('input[name='radio5']:checked').val();
            'sfqz': '0',  # 是否确诊
            'ycqksm': '',  # 异常情况说明
            'glqk': '0',  # 隔离情况
            'glksrq': '',  # 隔离开始日期
            'gljsrq': '',  # 隔离结束日期
            'tbly': 'sso',  # what's this?
            'glyy': '',  # 隔离原因
            'qtqksm': '',
            'sfjcqzsm': '',  # 是否接触确诊说明
            'sfjkqk': '0',
            'jkqksm': '',
            'sfmtbg': '',
            'qrlxzt': '',
            'xymc': xueyuan,
            'xssjhm': cellphone
        }

    header = {
        'Origin': 'http://yqtb.nwpu.edu.cn',
        'Referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp',
    }
    result = user.post('http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp',
                       data=data,
                       headers=header)
    print(result.text)
    if ("{\"state\":1}" not in result.text):
        print("error")
        exit(0)


def run():
    db = pymysql.connect(host=mysql_host, port=3306, user=mysql_username, passwd=mysql_passwd,
                         db="yqtb", charset="utf8")
    sql = """SELECT * FROM user"""
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        account = row[1]
        location = row[2]
        password = row[3]
        zip = row[4]
        hubei = row[5]
        name = row[6]
        inschool = row[7]

        user = login(account, password)

        getResult = user.get("http://yqtb.nwpu.edu.cn/wx/ry/jbxx_v.jsp")
        cellphone = (etree.HTML(getResult.content).xpath('//label[text()="手机号码："]/../../span/text()')[0])
        xueyuan = str(etree.HTML(getResult.content).xpath('//label[text()="学院/大类："]/../../span/text()')[0])
        name = str(etree.HTML(getResult.content).xpath('//label[text()="姓名："]/../../span/text()')[0])
        fxzt1 = re.findall(r"fxzt:'\d{1,}'", re.findall(r"var paramData.*fxzt:'\d{0,}'",
                                                        user.get(
                                                            'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp').text,
                                                        flags=0)[0])[0]
        fxzt = re.findall(r"\d{1,}", fxzt1)[0]

        yqtb(user, account, location, zip, hubei, name, xueyuan, cellphone, inschool, fxzt)

        time.sleep(30)
    else:
        print("login error")


if __name__ == '__main__':
    run()
