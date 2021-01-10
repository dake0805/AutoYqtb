def yqtb(user, account, location, zip, name, xueyuan, cellphone, inschool, fxzt):
    if (inschool == 1):
        zip = '1'
        location = '在学校'

    print(account + " " + location + " " + zip + " " + name + " " + xueyuan + " " + cellphone + " " + "fxzt" + fxzt)

    data = {
        'xasymt': '',
        'actionType': 'addRbxx',
        'userLoginId': account,
        'fxzt': fxzt,
        'userType': 2,
        'userName': name,
        'szcsbm': zip,  # 所在城市编码 2：在西安 3：其他
        'szcsmc': location,  # 所在城市名称
        'sfyzz': '0',  # var sfyzz =  $('input[name='radio5']:checked').val();
        'sfqz': '0',  # 是否确诊
        'tbly': 'sso',  # what's this?
        'qtqksm': '',
        'ycqksm': '',
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
