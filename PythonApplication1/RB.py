from bs4 import BeautifulSoup
import urllib.request
import pymysql.cursors 
import string
import re
from itertools import groupby

def R():
    connection = pymysql.connect(host='****',
                                 user='****',
                                 password='******',                         
                                 db='****',
                                 cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
    resp = urllib.request.urlopen("https://bookmaker-ratings.ru/tips/today/")
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    kom=[]
    res=[]
    data=[]
    ss=[]
    po=''
    ew=''
    for link in soup.find('div',class_='posts-block changeable-view view-grid').find_all('a', href=True):
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
                resp1 = urllib.request.urlopen(qwe.strip())
                soup1 = BeautifulSoup(resp1, from_encoding=resp1.info().get_param('charset'))
            for link1 in soup1.find_all('div',class_='bet-name'):
                s=link1.get_text()
                s.strip()
               
                if(s!="Итоговый"):
                    res.append( re.sub("^\s+|\n|\r|\s+$", '', s))
                    print( re.sub("^\s+|\n|\r|\s+$", '', s))
            for link2 in soup1.find_all('div',class_='name'):
                q=link2.get_text()
                q.strip()
                kom.append(re.sub("^\s+|\n|\r|\s+$", '',q))
                print(re.sub("^\s+|\n|\r|\s+$", '',q))
            for link3 in soup1.find_all('div',class_='date'):
                w=link3.get_text()
                w.strip()
               
                data.append( re.sub("^\s+|\n|\r|\s+$", '',w))
                print( re.sub("^\s+|\n|\r|\s+$", '',w))
        else:
             po = link.get_text().strip()

    
    try:
        i=0
        with connection.cursor() as cursor:
            while i < len(res):
              #  if(i % 2 == 0):
               #     j=i
               # if(len(kom[i])>10):
                    sql = """INSERT INTO rb (id,kom,data,res,result)
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



