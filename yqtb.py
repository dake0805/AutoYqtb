
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


