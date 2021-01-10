# contribute by xqj

from bs4 import BeautifulSoup


class RedisStoreInfo(object):
    data = dict()

    def __init__(self):
        soup = BeautifulSoup(open('202002281436.html', encoding='utf-8'), features='html.parser')
        city_infos = soup.find('tbody').findAll('tr')
        for index in range(len(city_infos)):
            if index < 3:
                continue
            city_detail = city_infos[index].findAll('td')
            # 去除首位空格
            self.data[city_detail[2].text.strip()] = city_detail[1].text

    def get_city_code(self, city_name):
        return self.data[city_name]


# demo

r = RedisStoreInfo()
print(r.get_city_code("北京市"))
print(r.get_city_code("安徽省淮南市田家庵区"))
print(r.get_city_code("东莞市"))
print(r.get_city_code("凤台县"))
