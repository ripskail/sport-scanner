from bs4 import BeautifulSoup
import urllib.request
import pymysql.cursors 
import string
import re

def ku():
   connection = pymysql.connect(host='****',
                                 user='****',
                                 password='******',                         
                                 db='****',
                                 cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
    resp = urllib.request.urlopen("https://kushvsporte.ru/freeforcats/sports/football?page=1")
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    kom=[]
    res=[]
    data=[]
    for link1 in soup.find_all('span',itemprop='name'):       
            kom.append(link1.get_text())
            print(link1.get_text())
    for link2 in soup.find_all('span',class_='col order-1 order-lg-3 typeBet'):
            res.append(link2.get_text())
            print(link2.get_text())
    for link3 in soup.find_all('span',itemprop="startDate"):
            data.append(link3.get_text())
            print(link3.get_text())
    for a in kom:
        #if len(a)< 11:
        if re.search(r'[A-Za-z]',a ):
            kom.remove(a)
    try:
        i=0
        with connection.cursor() as cursor:
            while i < len(res):
              #  if(i % 2 == 0):
               #     j=i
               # if(len(kom[i])>10):
                    sql = """INSERT INTO kushvsporte(id,kom,data,res,result)
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



