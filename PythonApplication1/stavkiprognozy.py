from bs4 import BeautifulSoup
import urllib.request
import pymysql.cursors 
import string
import re
from itertools import groupby


def st():
    connection = pymysql.connect(host='****',
                                 user='****',
                                 password='******',                         
                                 db='****',
                                 cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
    resp = urllib.request.urlopen("https://stavkiprognozy.ru/prognozy/football/")
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    kom=[]
    res=[]
    data=[]
    ss=[]
    po=''
    ew=''
    for link in soup.find('div',class_='section').find_all('a', class_='not-link single-announce-container'):
        ss.append(link['href'])
    vv = set(ss)
    for qwe in vv:
        print(qwe.strip())
        ew = qwe.strip()
        if(po!=ew):
            po = qwe.strip()
            if (link['href']!='#'):
                s=''
                q=''
                w=''
                resp1 = urllib.request.urlopen('https://stavkiprognozy.ru'+qwe)
                soup1 = BeautifulSoup(resp1, from_encoding=resp1.info().get_param('charset'))
            for link1 in soup1.find_all('span',class_='list-info-strong list-info-prop'):
                s=link1.get_text()
                s.strip()
                res.append(s)
                print(s)
            for link2 in soup1.find_all('div',class_='sinfor-main-panel-body-title'):
                q=link2.get_text()
                q.strip()
                kom.append(q)
                print(q)
            for link3 in soup1.find('div',class_='sinfor-main-panel-time-item d-none d-md-block').find_all_next('time',class_='time-item sinfor-main-panel-time-item'):
                w=link3['datetime']
                w.strip()
                data.append(w)
                print(w)
        else:
            po = link.get_text().strip()

    
    try:
        i=0
        with connection.cursor() as cursor:
            while i < len(res):
          #  if(i % 2 == 0):
           #     j=i
           # if(len(kom[i])>10):
                sql = """INSERT INTO stavkiprognozy (id,kom,data,res,result)
                VALUES (Null,'%(kom)s','%(data)s','%(res)s',Null)
                """%{"kom":kom[i],"data":data[i],"res":res[i]}
        # исполняем SQL-запрос
                cursor.execute(sql)
                connection.commit()
                print ("cursor.description: ", cursor.description)
                i+=1
           # else:
           #     i+=1


             
    finally:
    # Закрыть соединение (Close connection).      
        connection.close()




