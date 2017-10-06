import sqlite3
from datetime import timedelta
conn = sqlite3.connect('sp.db')
cur = conn.cursor()
query = cur.execute('''SELECT TIME from
                          RESULTS WHERE RACEID=5 AND AGE =65''')
results= cur.fetchall()
total = []
for rows in results:
    result =  (rows[0])
    total.append(result)
print (total )

#used this for help with working with times
#https://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times
times = total

print(str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), times)))/len(times))))