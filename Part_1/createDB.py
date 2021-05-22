import mysql.connector

myDB = mysql.connector.connect(host='localhost', user='root', passwd="amith")
myCursor = myDB.cursor()

def create():
    '''creates the database and the tasks and users tables'''
    try: myCursor.execute('drop database todo')
    except: pass
    myCursor.execute('create database todo')
    myCursor.execute('use todo')

    createStmt = """
    create table tasks
    (
        id int primary key auto_increment,
        task varchar(100) not null,
        due_by date not null,
        status varchar(20) not null,
        check(status in('Not started','In progress','Finished'))
    )
    """
    myCursor.execute(createStmt)
    
    createStmt = """
    create table users
    (
        userid varchar(50) primary key,
        access varchar(50),
        check(access in('read','write'))
    )
    """
    myCursor.execute(createStmt)
    
def populate():
    '''populates the creates tables with values'''
    myCursor.execute("insert into tasks values(0, 'LeanKloud', '2021-05-19', 'Finished')")
    myCursor.execute("insert into tasks values(0, 'Disk management project', '2021-05-28', 'In progress')")
    myCursor.execute("insert into tasks values(0, 'Flappy bird AI', '2021-05-30', 'Not started');")
    myDB.commit()

    myCursor.execute("insert into users values('amith001', 'write')")
    myCursor.execute("insert into users values('kumar002', 'read')")
    myDB.commit()
    
    
if __name__ == '__main__':
    create()
    populate()
    myCursor.close()
    myDB.close()