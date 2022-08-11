from bs4 import BeautifulSoup
from multiprocessing import Process
import urllib.request
import pymysql.cursors 
import string
import re
from vpliuse import vl
from stavkiprognozy import st
from RB import R
from kushvsporte import ku
from betonmobile import be
from odds import od

connection = pymysql.connect(host='****',
                                 user='****',
                                 password='******',                         
                                 db='****',
                                 cursorclass=pymysql.cursors.DictCursor)
print ("connect successful!!")
try:
    with connection.cursor() as cursor:
        sql = "TRUNCATE  vpliuse "
            # исполняем SQL-запрос
        cursor.execute(sql)
        sql = "TRUNCATE  stavkiprognozy"
            # исполняем SQL-запрос
        cursor.execute(sql)
        sql = "TRUNCATE  rb"
            # исполняем SQL-запрос
        cursor.execute(sql)
        sql = "TRUNCATE kushvsporte"
            # исполняем SQL-запрос
        cursor.execute(sql)
        sql = "TRUNCATE  betonmobile "
            # исполняем SQL-запрос
        cursor.execute(sql)
        sql = "TRUNCATE odds "
            # исполняем SQL-запрос
        cursor.execute(sql)
        connection.commit()
        print ("cursor.description: ", cursor.description)
finally:
    connection.close()

if __name__=='__main__':
    p1 = Process(target=vl)
    p1.start()
    p2 = Process(target=st)
    p2.start()
    p3 = Process(target=R)
    p3.start()
    p4 = Process(target=ku)
    p4.start()
    p5 = Process(target=be)
    p5.start()
    p6 = Process(target=od)
    p6.start()






