import sqlite3
import json

#generate devices.json for real-time-device-monitor from ipplan.db
#see https://gitlab.com/nibe-festival/real-time-device-monitor/

sql = '''SELECT name, ipv4_addr_txt
FROM host
'''

db = sqlite3.connect('/etc/ipplan.db')
cursor = db.cursor()

cursor.execute(sql,())

list = []
for row in cursor:
    data = {}
    data['host'] = row[1]
    switchname = row[0].split(".")[0]
    data['location'] = switchname
    data['port'] = '23'
    list.append(data)



print json.dumps(list, indent=4, sort_keys=True)
