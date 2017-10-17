import sqlite3
#database to store race info and result info
def createDatabase():
    try:
        conn = sqlite3.connect('sp.db')

        conn.execute('''DROP TABLE IF EXISTS RESULTS''')
        conn.execute('''DROP TABLE IF EXISTS RACES''')

        conn.execute('''CREATE TABLE RACES
                                         (
                                         RACEID INTEGER PRIMARY KEY AUTOINCREMENT ,
                                         LOCATION TEXT,                        
                                         ALTITUDE INT,
                                         TEMPU INT,
                                         HUMIDITY INT
                                         );''')
        conn.execute('''CREATE TABLE RESULTS
                         (
                         RACEID INTEGER,
                         AGE INT,
                         GENDER TEXT,                        
                         TIME INT,
                         FOREIGN KEY(RACEID) REFERENCES RACES(RACEID)
                         );''')

        conn.close()
    except sqlite3.OperationalError as err:
        print(err)
        print("The database already exists")
def createRace(location, altitude, temperature, humidity):

    conn = sqlite3.connect('sp.db')
    c = conn.cursor()
    c.execute('''INSERT INTO RACES
                         (LOCATION, ALTITUDE, TEMPU, HUMIDITY)\
                      VALUES(?,?,?,? )''',
                 (location, altitude, temperature, humidity))

    raceID = c.lastrowid
    conn.commit()
    conn.close()
    return(raceID)

def addRows(string, race):

    age = string.split(" ")[0]

    gender = string.split(" ")[1]

    time = string.split(" ")[2]

    conn = sqlite3.connect('sp.db')

    conn.execute('''INSERT INTO RESULTS
                     (RACEID, AGE, GENDER, TIME)\
                  VALUES(?,?,?,? )''',
                 (race, age, gender, time))
    conn.commit()
    conn.close()
def displayRows():
    conn = sqlite3.connect('sp.db')
    cursor = conn.execute('''SELECT RACEID, AGE, GENDER, TIME from
                          RESULTS WHERE RACEID = 11''')
    print("Here are all the table rows")
    for row in cursor:
        print("RACEID=", row[0], "AGE=", row[1], "GENDER=", row[2], "TIME=", row[3])
#displayRows()
def displayRACERows():
    conn = sqlite3.connect('sp.db')
    cursor = conn.execute('''SELECT RACEID, LOCATION, ALTITUDE, TEMPU, HUMIDITY from
                          RACES''')

    for row in cursor:
        print("RACEID=", row[0], "LOCATION=", row[1], "ALTITUDE=", row[2], "TEMPU=", row[3], "HUMIDITY=", row[4])
displayRACERows()
def deleateRows():

        conn = sqlite3.connect('sp.db')

        cursor = conn.execute('DELETE FROM RACES WHERE RACEID = 12')
        # uses rowcount to see if a row was affected
        deleteStatus = (cursor.rowcount)
        # depending on if rows were affected or not a message will print
        if deleteStatus == 0:
            print("This product is not in the database")
        elif deleteStatus == 1:
            print("Row was deleted")
        conn.commit()
        conn.close()