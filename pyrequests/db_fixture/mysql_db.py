#coding=utf-8
from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
import pymysql.cursors



host = '127.0.0.1'
port = '3306'
db   = 'guest'
user = 'root'
password = 'root'
class DB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=host,
                                port=int(port),
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print('Mysql Error %d: %s' % (e.args[0], e.args[1]))

    def clear(self,table_name):
        #real_sql = 'truncate table ' + table_name + ';'
        real_sql = 'delete from ' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.conn.commit()

    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
            key  = ','.join(str(table_data.keys()))
            value = ','.join(str(table_data.values()))
            real_sql = "INSERT INTO "+ table_name + "(" + key + ") VALUES (" + value + ")"

            with self.conn.cursor() as curssor:
                curssor.execute(real_sql)

            self.conn.commit()
    def close(self):
        self.conn.close()

if __name__ == '__main__':

    db = DB()
    table_name = "login_event"
    data = {'id':1,'name':'红米','limit':2000,'status':1,'`address`':'北京',
            'start_time':'2016-08-20 00:25:42','end_time':'2017-09-21 10:00:00'}
    table_name2 = "login_guest"
    data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
