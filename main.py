import re
import time

import pymysql

from login import *
from yqtb import yqtb


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
        # hubei = row[5]
        # name = row[6]
        inschool = row[6]

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

        yqtb(user, account, location, zip, name, xueyuan, cellphone, inschool, fxzt)

        time.sleep(30)
    else:
        print("login error @ main.py 45")


if __name__ == '__main__':
    run()
