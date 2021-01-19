def yqtb(user, account, location, zip, name, xueyuan, cellphone, inschool, fxzt):
    if (inschool == 1):
        zip = '1'
        location = '在学校'

    print(account + " " + location + " " + zip + " " + name + " " + xueyuan + " " + cellphone + " " + "fxzt" + fxzt)
    data = {
        'sfczbcqca': '',
        'czbcqcasjd': '',
        'sfczbcfhyy': '',
        'czbcfhyysjd': '',
        'actionType': 'addRbxx',
        'userLoginId': account,
        'fxzt': fxzt,
        'userType': '2',
        'userName': name,
        'szcsbm': zip,  # 所在城市编码 2：在西安 3：其他
        'szcsmc': location,  # 所在城市名称
        'sfjt': '0',
        'sfjtsm': '',
        'sfjcry': '0',
        'sfjcrysm': '',
        'sfjcqz': '0',
        'sfyzz': '0',
        'sfqz': '0',
        'ycqksm': '',
        'glqk': '0',
        'glksrq': '',
        'gljsrq': '',
        'tbly': 'sso',
        'glyy': '',
        'qtqksm': '',
        'sfjcqzsm': '',
        'sfjkqk': '0',
        'jkqksm': '',
        'sfmtbg': '',
        'qrlxzt': '',
        'xymc': xueyuan,
        'xssjhm': cellphone
    }
    print(data)
    header = {
        'Origin': 'http://yqtb.nwpu.edu.cn',
        'Referer': 'http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    result = user.post('http://yqtb.nwpu.edu.cn/wx/ry/ry_util.jsp',
                       data=data,
                       headers=header)
    print(result.text)
    if ("{\"state\":1}" not in result.text):
        print("error")
        exit(0)
