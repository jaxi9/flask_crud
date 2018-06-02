# coding=utf-8

# from flask import Flask
import flask
import pymysql
import logging

app = flask.Flask(__name__)
student = {}

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return flask.render_template('index.html')


# 查询所有学生信息
@app.route('/list')
def list():
    db = pymysql.connect("localhost","root","root","test_01")
    cursor = db.cursor()
    sql = "select * from tb_student"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    db.close()
    result = {}
    students = []
    for i in data:
        student = {}
        student['id'] = i[0]
        student['name'] = i[1]
        student['age'] = i[2]
        student['sex'] = i[3]
        student['score'] = i[4]
        print(student)
        students.append(student)
    result['students'] = students
    print students
    print result
    # return json.dumps(result)
    # datas = json.dumps(result)
    return flask.render_template('list.html',result=result)


# 添加学生信息
@app.route('/add')
def add():
    print '---------add--------'
    return flask.render_template('add.html')

@app.route('/select/<id>')
def select(id):

    print '---------select--------'
    db = pymysql.connect("localhost","root","root","test_01")
    cursor = db.cursor()
    sql = "select * from tb_student where id = %s"
    cursor.execute(sql,id)
    data = cursor.fetchone()
    db.close()
    print 'data={}',data
    return flask.render_template('edit.html',data=data)


# 保存学生信息
@app.route('/save',methods={'post'})
def save():
    name = flask.request.form.get('name')
    sex = flask.request.form.get('sex')
    age =flask.request.form.get('age')
    score = flask.request.form.get('score')
    db = pymysql.connect("localhost","root","root","test_01")
    cursor = db.cursor()
    sql = "insert into tb_student(name,sex,age,score)values (%s,%s,%s,%s)"
    try:
        cursor.execute(sql,(name,sex,age,score))
        db.commit()
        logging.info("保存成功！")
    except:
        db.rollback()
        logging.info("保存失败")
    db.close()
    print '----------save------------'
    return flask.redirect('/list')


# 修改学生信息
@app.route('/update/<id>',methods={'post'})
def update(id):
    print "--------update-----------"
    name = flask.request.form.get('name')
    sex = flask.request.form.get('sex')
    age = flask.request.form.get('age')
    score = flask.request.form.get('score')
    db = pymysql.connect("localhost","root","root","test_01")
    cursor = db.cursor()
    sql = "update tb_student set name = %s,sex=%s,age=%s,score=%s where id = %s"
    try:
        cursor.execute(sql,(name,sex,age,score,id))
        db.commit()
        logging.info("修改成功!")
    except:
        db.rollback()
        logging.info("修改失败！")
    db.close()

    return flask.redirect("/list")


# 删除学生信息
@app.route('/delete/<id>')
def delete(id):
    print '------------------'
    db = pymysql.connect("localhost","root","root","test_01")
    cursor = db.cursor()
    sql = "delete from tb_student where id = %s"
    try:
        cursor.execute(sql,id)
        db.commit()
        logging.info("删除成功！")
    except:
        db.rollback()
        logging.info("删除失败！")
    db.close()
    return flask.redirect('/list')


if __name__ == '__main__':
    app.run()
