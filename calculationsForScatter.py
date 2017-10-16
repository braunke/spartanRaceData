import sqlite3
#grabs race times and altitude
def getRaceTimes(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME , ALTITUDE from
                                      RESULTS 
                                      INNER JOIN RACES on RACES.RACEID = RESULTS.RACEID WHERE RACES.RACEID=? ''', (race,))
    results = cur.fetchall()
    total = []
    lastTimeAdded = ""
    for rows in results:
        result = (rows[0])
        split = result.split(':')
        # handles if a time does not have hours
        if len(split) < 3:
            split.insert(0, '0')
        roundedTimeToAdd = split[0] + ":" + split[1]
        if roundedTimeToAdd != lastTimeAdded:
            lastTimeAdded = roundedTimeToAdd
            #converts to a number I can use of the graph
            ftr = [3600, 60]
            times = sum([a * b for a, b in zip(ftr, map(int, roundedTimeToAdd.split(':')))])
            result = times / 3600
            total.append((result, rows[1]))
    return total
#grabs race times and humidity data
def getRaceHumidityTimes(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME , Humidity from
                                      RESULTS 
                                      INNER JOIN RACES on RACES.RACEID = RESULTS.RACEID WHERE RACES.RACEID=? ''', (race,))
    results = cur.fetchall()
    total = []
    lastTimeAdded = ""
    for rows in results:
        result = (rows[0])
        split = result.split(':')
        # handles if a time does not have hours
        if len(split) < 3:
            split.insert(0, '0')
        roundedTimeToAdd = split[0] + ":" + split[1]
        if roundedTimeToAdd != lastTimeAdded:
            lastTimeAdded = roundedTimeToAdd
            # converts to a number I can use of the graph
            ftr = [3600, 60]
            times = sum([a * b for a, b in zip(ftr, map(int, roundedTimeToAdd.split(':')))])
            result = times / 3600
            total.append((result, rows[1]))
    return total
def getRaceTempTimes(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME , Tempu from
                                      RESULTS 
                                      INNER JOIN RACES on RACES.RACEID = RESULTS.RACEID WHERE RACES.RACEID=? ''', (race,))
    results = cur.fetchall()
    total = []
    lastTimeAdded = ""
    for rows in results:
        result = (rows[0])
        split = result.split(':')
        # handles if a time does not have hours
        if len(split) < 3:
            split.insert(0, '0')
        roundedTimeToAdd = split[0] + ":" + split[1]
        if roundedTimeToAdd != lastTimeAdded:
            lastTimeAdded = roundedTimeToAdd
            # converts to a number I can use of the graph
            ftr = [3600, 60]
            times = sum([a * b for a, b in zip(ftr, map(int, roundedTimeToAdd.split(':')))])
            result = times / 3600
            total.append((result, rows[1]))
    return total
#takes in a race index to only grab a certain races info from the list
def getItAllAlt(raceIndex):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    races = []
    for raceid in raceids:
        race = getRaceTimes(raceid[0])
        races.append(race)
    return races[raceIndex]
def getItAllHumidity(raceIndex):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    races = []
    for raceid in raceids:
        race = getRaceHumidityTimes(raceid[0])
        races.append(race)
    return races[raceIndex]
#getItAllHumidity(1)
def getItAllTemp(raceIndex):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    races = []
    for raceid in raceids:
        race = getRaceTempTimes(raceid[0])
        races.append(race)
    return races[raceIndex]
