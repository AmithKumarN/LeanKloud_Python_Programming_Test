import mysql.connector

myDB = mysql.connector.connect(host='localhost', user='root', passwd="amith")
myCursor = myDB.cursor()

myCursor.execute('create database todo')
myCursor.execute('use todo')

createStmt = """
create table tasks
(
    id int primary key,
    task varchar(100) not null,
    due_by date not null,
    status varchar(20) not null,
    check(status in('Not started','In progress','Finished'))
)
"""
myCursor.execute(createStmt)