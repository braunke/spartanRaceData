import sqlite3
def getTeenTotals(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME  FROM
                                  RESULTS WHERE RACEID=? AND (AGE <20)''', (race,))
    results = cur.fetchall()
    total = 0
    for row in results:
        total += 1
    return total
def getAllTeen():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()

    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    racesTotal = 0
    for raceid in raceids:
        race = int(getTeenTotals(raceid[0]))
        racesTotal += race
    print(racesTotal)
    return racesTotal
getAllTeen()
def get20Totals(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME  FROM
                                  RESULTS WHERE RACEID=? AND (AGE >= 20 AND AGE <30)''', (race,))
    results = cur.fetchall()
    total = 0
    for row in results:
        total += 1
    return total
def getAll20():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()

    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    racesTotal = 0
    for raceid in raceids:
        race = int(get20Totals(raceid[0]))
        racesTotal += race
    print(racesTotal)
    return racesTotal
getAll20()
def get30Totals(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME  FROM
                                  RESULTS WHERE RACEID=? AND (AGE >= 30 AND AGE <40)''', (race,))
    results = cur.fetchall()
    total = 0
    for row in results:
        total += 1
    return total
def getAll30():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()

    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    racesTotal = 0
    for raceid in raceids:
        race = int(get30Totals(raceid[0]))
        racesTotal += race
    print(racesTotal)
    return racesTotal
getAll30()
def getAgGroupTotals(race, minAge,maxAge):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT TIME  FROM
                                  RESULTS WHERE RACEID=? AND AGE BETWEEN ? AND ?''', (race,minAge,maxAge,))
    results = cur.fetchall()
    total = 0
    for row in results:
        total += 1
    return total
def getAllAgeGroup(minAge, maxAge):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    racesTotal = 0
    for raceid in raceids:
        race = int(getAgGroupTotals(raceid[0],minAge,maxAge))
        racesTotal += race
    print(racesTotal)
    return racesTotal
getAllAgeGroup(40,49)