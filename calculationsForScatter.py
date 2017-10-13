import sqlite3
from datetime import timedelta
#grabs race time averages and altitude
def getRaceTimes(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME , ALTITUDE from
                                      RESULTS 
                                      INNER JOIN RACES on RACES.RACEID = RESULTS.RACEID WHERE RACES.RACEID=? ''', (race,))
    results = cur.fetchall()
    total = []
    for rows in results:
        result = (rows[0])
        split = result.split(':')
        # handles if a time does not have hours
        if len(split) < 3:
            split.insert(0, '0')
            s = ":"
            result = s.join(split)

        averageS = result[:result.rfind(".")]
        ftr = [3600, 60, 1]
        times = sum([a * b for a, b in zip(ftr, map(int, averageS.split(':')))])
        result = times / 3600
        total.append((result, rows[1]))

    # used this for help with working with times
    # https://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times


    return total
def getItAll(raceIndex):
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
#getItAll(0)