import sqlite3
from datetime import timedelta
def getRaceTimes(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME  from
                                      RESULTS WHERE RACEID=? ''', (race,))
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
        total.append(result)
    # used this for help with working with times
    # https://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times
    times = total
    average = (str(timedelta(seconds=sum(
        map(lambda f: int(f[0]) * 3600 + int(f[1]) * 60 + int(f[2]), map(lambda f: f.split(':'), times))) / len(
        times))))
    # rounds to whole seconds
    averageS = average[:average.rfind(".")]
    ftr = [3600, 60, 1]
    times = sum([a * b for a, b in zip(ftr, map(int, averageS.split(':')))])
    final = times / 3600
    conn = sqlite3.connect('sp.db')
    cursor = conn.execute('''SELECT ALTITUDE from
                                          RACES WHERE RACEID=?''', (race,))
    altitude = ''
    for row in cursor:
        altitude = (row[0])

    return final, altitude


def getItAll():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()

    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    races = []
    for raceid in raceids:
        race = getRaceTimes(raceid[0])
        races.append(race)
    print(races)
    return races
getItAll()