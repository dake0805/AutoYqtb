from lxml import etree

import requests
from http.cookiejar import CookieJar


def login(url):
    user = requests.session()

    getResult = user.get("https://uis.nwpu.edu.cn/cas/login")
    JSESSIONID = dict(getResult.cookies)['JSESSIONID']
    print(JSESSIONID)
    form_data_lt = str(etree.HTML(getResult.content).xpath('//input[@name="lt"]/@value')[0])
    header = {
        "Origin": "https://uis.nwpu.edu.cn",
        "Referer": "https://uis.nwpu.edu.cn/cas/login",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    postData = {
        "username": "1",
        "password": "1",
        "imageCodeName": "",
        "lt": form_data_lt,
        "_eventId": "submit"
    }
    response = user.post("https://uis.nwpu.edu.cn/cas/login;jsessionid=" + JSESSIONID, data=postData, headers=header)
    cookie = response.cookies
    return cookie


def yqtb(cookie):


if __name__ == "__main__":
    cookie = login(
        "https://uis.nwpu.edu.cn/cas/login?service=http%3A%2F%2Fyqtb.nwpu.edu.cn%2F%2Fsso%2Flogin.jsp%3FtargetUrl%3Dbase64aHR0cDovL3lxdGIubndwdS5lZHUuY24vL3d4L3J5L2pyc2IuanNw")
    yqtb(cookie)
