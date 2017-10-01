import sqlite3

def createDatabase():
    try:
        conn = sqlite3.connect('results.db')
        conn.execute('''CREATE TABLE RESULTS
                         (
                         AGE INT,
                         GENDER TEXT,
                         
                         TIME INT
                         );''')
        conn.close()
    except sqlite3.OperationalError:
        print("The database already exists")

#createDatabase()

def addRows(string):

    age = string.split(" ")[0]

    gender = string.split(" ")[1]

    time = string.split(" ")[2]

    conn = sqlite3.connect('results.db')

    conn.execute('''INSERT INTO RESULTS
                     (AGE, GENDER, TIME)\
                  VALUES(?,?,? )''',
                 (age, gender, time))
    conn.commit()
    conn.close()
def displayRows():
    conn = sqlite3.connect('results.db')
    cursor = conn.execute('''SELECT AGE, GENDER,  TIME from
                          RESULTS''')
    print("Here are all the table rows")
    for row in cursor:
        print("AGE =", row[0], "GENDER=", row[1], "TIME=", row[2])
displayRows()