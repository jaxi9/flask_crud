# coding=utf-8
import pymysql


def create_table():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "test_01")
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    # 创建数据库表
    sql = '''create table tb_student(
    id int primary key auto_increment,
    name varchar(20) not null,
    age int,
    sex char(1),
    score float 
    )'''

    # 使用execute()执行sql
    cursor.execute(sql)

    # 关闭数据库连接
    db.close()



if __name__ == '__main__':
    create_table()