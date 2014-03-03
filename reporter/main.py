from reporter import configmanager, sqlitemanager
import time
import datetime

#print (str(datetime.datetime.now().strftime("%Y-%m-%d")))
# c = configmanager.loadconfig()
# d = sqlitemanager
#
# if c.create_table == "true":
#     d.createTable(c.sqlitepath, c.query)
#
# statuses = d.getAllStatuses(c.sqlitepath)
# for st in statuses:
#     print(st.id)
#     print(st.status)
#     print(st.timestamp)


now = datetime.datetime.now()+datetime.timedelta(1)

now_day_1 = now - datetime.timedelta(days=now.weekday())


print [(now_day_1 + datetime.timedelta(days=d)).strftime("%Y-%m-%d") for d in range(5)]