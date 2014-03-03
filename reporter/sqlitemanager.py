import sqlite3 as sqlite
import time
import datetime

class Status:
    id = 0
    status=""
    date=""

def createTable(db, query):
    executeCommitQuery(db, query)

def insertStatus(db, status):
    query = "INSERT INTO status (status, date) VALUES ('" + status + "'" + ",'" + str(datetime.datetime.now()) + "');"
    executeCommitQuery(db, query)

def getAllStatuses(db):
    records = executeQuery(db, "SELECT * FROM status;")
    statuses = []
    for record in records:
         statuses.append(dbRowToStatus(record))

    return statuses

def loadStatusesByCurrentDay(db):
    return loadStatusesByDay(db, str(datetime.datetime.now().strftime("%Y-%m-%d")))

def loadStatusesByDay(db, day):
    records = executeQuery(db, "SELECT * FROM status WHERE date LIKE '" + day + "%';")
    statuses = []
    for record in records:
         statuses.append(dbRowToStatus(record))
    return statuses

def updateStatus(db, id, status):
    pass

def removeStatus(db, id):
    pass

def loadStatusesByPeriod(db, startdate, enddate):
    return []

def loadCurrentWeekStatuses(db):
    now = datetime.datetime.now()+datetime.timedelta(1)
    now_day_1 = now - datetime.timedelta(days=now.weekday())
    days = [(now_day_1 + datetime.timedelta(days=d)).strftime("%Y-%m-%d") for d in range(5)]
    statuses={}
    for day in days:
        statuses[day] = loadStatusesByDay(db, day)
    return statuses

########################################

def dbRowToStatus(row):
    status = Status()
    status.id = row[0]
    status.status = row[1]
    status.date = row[2]
    return status

def executeQuery(db, query):
    try:
        con = sqlite.connect(db)
        cursor = con.execute(query)
        return cursor.fetchall()
    except sqlite.Error as e:
        print ("Error %s:" % e.args[0])
    finally:
        if con:
            con.close()

def executeCommitQuery(db, query):
    try:
        con = sqlite.connect(db)
        con.execute(query)
        con.commit()
    except sqlite.Error as e:
        print ("Error %s:" % e.args[0])
    finally:
        if con:
            con.close()