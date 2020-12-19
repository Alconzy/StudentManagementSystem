import sqlite3


def init():
    db = sqlite3.connect('student.db')
    db.execute('create table if not exists stu (name varchar(20), age varchar(20), phone varchar(20), '
               'address varchar(20))')
    db.execute("insert into stu values('Tim', '21', '13575328905', 'New York')")
    db.execute("insert into stu values('Dalton', '23', '15987635482', 'Denver')")
    db.execute("insert into stu values('Kelly', '19', '13657423150', 'Chicago')")
    db.execute("insert into stu values('Torres', '20', '15789643025', 'Canberra')")
    db.execute("insert into stu values('Lucas', '18', '15489653254', 'Fremantle')")
    db.commit()
    db.close()


def find_all():
    db = sqlite3.connect('student.db')
    result = db.execute('select * from stu')
    stu = []
    for row in result:
        stu.append(row)

    db.close()
    return stu


def add(name, age, phone, address):
    db = sqlite3.connect('student.db')
    db.execute("insert into stu values('%s', '%s', '%s', '%s')" % (name, age, phone, address))
    db.commit()
    db.close()


def find_by_name(name):
    db = sqlite3.connect('student.db')
    result = db.execute("select * from stu where name='%s'" % name)
    stu = next(result)
    db.close()
    return stu


def delete_by_name(name):
    db = sqlite3.connect('student.db')
    db.execute("delete from stu where name= '%s'" % name)
    db.commit()
    db.close()


def update(name, age, phone, address):
    db = sqlite3.connect('student.db')
    db.execute("update stu set age='%s', phone='%s', address='%s' where name='%s'" % (age, phone, address, name))
    db.commit()
    db.close()


if __name__ == '__main__':
    init()
