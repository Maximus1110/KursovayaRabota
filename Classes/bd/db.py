import sqlite3


def addItemToDB(data):

    con=sqlite3.connect('Classes/bd/mainDB.db')
    cur=con.cursor()

    cur.execute(f'SELECT * FROM Elem')
    value=cur.fetchall()
    
    for item in value:
        if(item[0]==data.index):
            return False

    cur.execute(f"""INSERT INTO Elem VALUES ('{data.index}', 
    '{data.name}', '{data.text}','{data.createTime}',
    '{data.data}','{data.startTime}','{data.endTime}',
    '{data.everyWeek}','{data.addToCalendar}')""")

    con.commit()
    return True

def getItemDataFromDB():
    con=sqlite3.connect('Classes/bd/mainDB.db')
    cur=con.cursor()

    
    cur.execute(f'SELECT * FROM Elem')
    value=cur.fetchall()
    

    return value

def addButtonNameToDB(name):
    con=sqlite3.connect('Classes/bd/mainDB.db')
    cur=con.cursor()


    cur.execute(f"""INSERT INTO Button VALUES ('{name}')""")

    con.commit()
    return True

def getButtonNameFromDB():
    con=sqlite3.connect('Classes/bd/mainDB.db')
    cur=con.cursor()

    
    cur.execute(f'SELECT * FROM Button')
    value=cur.fetchall()
    return value

def deleteItemFromDB(data):
    con=sqlite3.connect('Classes/bd/mainDB.db')
    cur=con.cursor()
    
    sql_update_query = f"""DELETE from Elem where `index` = '{data.index}'"""
    cur.execute(sql_update_query)
    con.commit()


    return True

def deleteButtonFromDB(name):
    con=sqlite3.connect('Classes/bd/mainDB.db')
    cur=con.cursor()
    
    sql_update_query = f"""DELETE from Button where `name` = '{name}'"""
    cur.execute(sql_update_query)
    con.commit()


    return True




