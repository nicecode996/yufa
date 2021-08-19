#! usr/bin/env python3
# coding=utf-8
import pymysql

import pymysql
conn = pymysql.connect(host='127.0.0.1', user = "root", p++asswd="123456", db="testdb", port=3310, charset="utf8")
cur = conn.cursor()
#sql语句
sql = "insert into tb_user(userName, birth) value(%s, %s)"
#数据
person = [['小军', '1993-06-05'], ['小明', '1993-04-03']]

for i in range(len(person)):
    param = tuple(person[i])
    #执行sql语句
    count = cur.execute(sql, param)
    #判断是否成功
    if count > 0:
        print("添加数据成功！\n")
#提交事务
conn.commit()

#查询数据
cur.execute("select * from tb_user")
#获取数据
users = cur.fetchall();

for i in range(len(users)):
    print(users[i]);

#关闭资源连接
cur.close()
conn.close()
print("数据库断开连接！");
