from bs4 import BeautifulSoup
import redis


class RedisStoreInfo(object):
    def __init__(self):
        self.redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        self.redis_conn = redis.Redis(connection_pool=self.redis_pool)

        soup = BeautifulSoup(open('202002281436.html', encoding='utf-8'), features='html.parser')
        city_infos = soup.find('tbody').findAll('tr')
        for index in range(len(city_infos)):
            if index < 3:
                continue
            city_detail = city_infos[index].findAll('td')
            # 去除首位空格
            self.redis_conn.set(city_detail[2].text.strip(), city_detail[1].text)

    def get_xzqh(self, city_name):
        if not self.redis_conn.get(city_name) is None:
            return self.redis_conn.get(city_name).decode()
        else:
            return None


# demo

r = RedisStoreInfo()
print(r.get_xzqh("北京市"))
print(r.get_xzqh("田家庵区"))
print(r.get_xzqh("东莞市"))
print(r.get_xzqh("凤台县"))
