from bs4 import BeautifulSoup
import urllib.request
import pymysql.cursors 
import string
import re

def vl():
    connection = pymysql.connect(host='****',
                                 user='****',
                                 password='******',                         
                                 db='****',
                                 cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
    resp = urllib.request.urlopen("https://vpliuse.ru/stavki")
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    kom=[]
    res=[]
    data=[]
    for link1 in soup.find_all('span',class_='tipster__title-text'):
        kom.append( re.sub("^\s+|\n|\r|\s+$", '', link1.get_text()))
        print(link1.get_text())
    for link2 in soup.find_all('div',class_='tipster__meta text-orange'):
        a = link2.get_text()
        res.append(a.split('\n')[2])
        print(link2.get_text())
        data.append(a.split('\n')[1])

    try:
        i=0
        with connection.cursor() as cursor:
            while i < len(res):
          #  if(i % 2 == 0):
           #     j=i
           # if(len(kom[i])>10):
                sql = """INSERT INTO vpliuse (id,kom,data,res,result)
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





