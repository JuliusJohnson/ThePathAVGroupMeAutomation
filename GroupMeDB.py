from pprint import pprint
import sendGroupme
import sqlite3
from pprint import pprint
import sendEmail

conn = sqlite3.connect('/home/julius/Documents/python/projects/thepathDB/PlanningCenter')
connectionCursor = conn.cursor()

def getServiceOrder():
    serviceItems = []
    for row in connectionCursor.execute("SELECT ifnull(Title || ' - ' || Description, title) AS Item FROM PlanningCenterItems WHERE Service_Position = 'during' AND Item_Type != 'header' AND (RelatedPlan)=(SELECT MAX(RelatedPlan) FROM PlanningCenterItems) ORDER BY Sequence ASC"):
        serviceItems.append(row[0])
    return str('\n'.join(map(str,serviceItems)))

def getPreService():
    serviceItems = []
    for row in connectionCursor.execute("SELECT ifnull(Title || ' - ' || Description, title) AS Item FROM PlanningCenterItems WHERE Service_Position = 'pre' AND Item_Type != 'header' AND (RelatedPlan)=(SELECT MAX(RelatedPlan) FROM PlanningCenterItems) ORDER BY Sequence ASC"):
        serviceItems.append(row[0])
    return str('\n'.join(map(str,serviceItems)))

sendEmail.sendMail(getPreService(),getServiceOrder())
#sendGroupme.send(getServiceOrder())
pprint(getServiceOrder())