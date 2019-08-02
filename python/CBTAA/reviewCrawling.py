import urllib.request
from bs4 import BeautifulSoup


html = 'https://www.siksinhot.com/P/'
num = 256500
result = []
for i in range(1001,4000):
    soup = BeautifulSoup(urllib.request.urlopen(html+str(num + i)), features='html.parser')
    temp = soup.find_all(class_="score_story")
    n = 0
    for j in temp:
        tmp = j.get_text()
        print(tmp)
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
