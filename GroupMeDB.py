from pprint import pprint
import sendGroupme
import sqlite3
from pprint import pprint

conn = sqlite3.connect('/home/julius/Documents/python/projects/thepathDB/PlanningCenter')
connectionCursor = conn.cursor()

def getServiceOrder():
    serviceItems = []
    for row in connectionCursor.execute("SELECT Title FROM PlanningCenterItems WHERE substr(DateAdded,1,10)=(SELECT substr(DateAdded,1,10)FROM PlanningCenterItems)ORDER BY Sequence ASC"):
        serviceItems.append(row[0])
    return str('\n'.join(map(str,serviceItems)))

sendGroupme.send(getServiceOrder())
pprint(getServiceOrder())