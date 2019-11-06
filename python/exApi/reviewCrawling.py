import urllib.request
from bs4 import BeautifulSoup
import pymysql

def run():
    html = 'https://www.siksinhot.com/P/'
    num = 256500
    flag = 1
    result = []
    for i in range(6001,20000):
        soup = BeautifulSoup(urllib.request.urlopen(html+str(num + i)), features='html.parser')
        temp = soup.find_all(class_="score_story")
        n = 0
        print(float(flag/5000) * 100)
        flag += 1
        for j in temp:
            tmp = j.get_text()
            #print(tmp)
            if '@' in tmp:
                pass
            elif ('0' or '1' or '2' or '3' or '4' or '5') in tmp.split(' ')[0]:
                tmp = tmp.replace(tmp.split(' ')[0], '')
            elif len(tmp) > 50:
                """
                for i in set(text02):
                    textmax.append(text02.count(i))
                if max(textmax) > 8:
                    print('중복된 문자가 너무 많으므로 예외')
                """
                tmp = tmp.replace('\n', ' ')
                result.append(tmp)

    for i in result:
        tempMax = []
        print(i)
        for j in set(i):
            tempMax.append(i.count(j))
        if max(tempMax) > 8:
            result.remove(i)

    insDB(result)

def insDB(_list):
    conn = pymysql.connect(host='localhost', user='root', password='qwe123!!@@', db='menu', charset='utf8')
    cur = conn.cursor()
    sql_insert_qurey = "INSERT INTO menu.review VALUES (%s, %s, %s, %s)"
    row = 93

    for i in _list:
        cur.execute(sql_insert_qurey,
        (str(row), str(i), 'None', 'None')
        )
        row = row + 1
    conn.commit()

if __name__ == "__main__":
    run()
