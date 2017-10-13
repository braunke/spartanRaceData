import sqlite3
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
    return racesTotal
