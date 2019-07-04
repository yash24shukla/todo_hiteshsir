# this is backend coding part where we are fetching the database
import sqlite3

db = 'todo_task.db'
table_name = 'tasks'
conn = sqlite3.connect(db)
c = conn.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID INTEGER PRIMARY KEY AUTOINCREMENT, TaskName text)'
    c.execute(sql)


def data_entry(task):
    sql = "INSERT INTO " + table_name + " (TaskName) VALUES (?)"

    c.execute("INSERT INTO " + table_name + " (TaskName) VALUES (?)", [task])
    print("Task added")
    conn.commit()


def printData():
    sql = "SELECT * FROM " + table_name
    c.execute(sql)

    for row in c.fetchall():
        print(row[0],"-->",row[1])
def deleteTask(index):
    c.execute('DELETE FROM ' + table_name + ' WHERE ID=?', (index,))
    print("Task Deleted")

def closeCursor():
    c.close()
    conn.close()