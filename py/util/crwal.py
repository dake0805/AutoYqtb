from bs4 import BeautifulSoup

# 通过传入城市的字符串，返回对应的行政区号
def get_xzqh(city_name):
    soup = BeautifulSoup(open('202002281436.html', encoding='utf-8'), features='html.parser')
    city_infos = soup.find('tbody').findAll('tr')
    for city_info in city_infos:
        city_detail = city_info.findAll('td')
        # 去除首位空格
        if city_detail[2].text.strip() == city_name:
            return city_detail[1].text

