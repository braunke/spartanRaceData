import sqlite3
from datetime import timedelta
#grabs all the average times from each race
def getAInfo(race):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    cur.execute('''SELECT TIME  from
                              RESULTS WHERE RACEID=? ''',(race,))
    results= cur.fetchall()
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
    #used this for help with working with times
    #https://stackoverflow.com/questions/12033905/using-python-to-create-an-average-out-of-a-list-of-times
    times = total
    average =(str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), times)))/len(times))))
    #rounds to whole seconds
    averageS = average[:average.rfind(".")]
    ftr = [3600, 60, 1]
    times = sum([a * b for a, b in zip(ftr, map(int, averageS.split(':')))])
    final = times/3600
    conn = sqlite3.connect('sp.db')
    cursor = conn.execute('''SELECT LOCATION from
                                  RACES WHERE RACEID=?''',(race,))
    location = ''
    for row in cursor:
        location = (row[0])

    return final, location

#collects all the data and puts it in a list
def getItAll():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()

    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    races = []
    for raceid in raceids:
        race = getAInfo(raceid[0])
        races.append(race)
    print(races)
    return races
getItAll()
#calculates the average race times for males and females
def getAverageGender(race, gender):
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    race = race
    gender = gender
    cur.execute('''SELECT TIME  from
                                    RESULTS WHERE RACEID=? and GENDER=?''', (race,gender,))
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

    return final
def getAllMale():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    gender = "M"
    raceids = cur.fetchall()
    maleRaces = []
    for raceid in raceids:
        race = getAverageGender(raceid[0], gender,)
        maleRaces.append(race)
    return maleRaces
def getAllFemale():
    conn = sqlite3.connect('sp.db')
    cur = conn.cursor()
    cur.execute('''SELECT RACEID  from
                                  RACES ''', )
    raceids = cur.fetchall()
    gender = "F"
    femaleRaces = []
    for raceid in raceids:
        race = getAverageGender(raceid[0], gender)
        femaleRaces.append(race)
    print(femaleRaces)
    return femaleRaces

def getRaceList():
    conn = sqlite3.connect('sp.db')
    cursor = conn.execute('''SELECT DISTINCT LOCATION from
                                      RACES ''',)
    locationList = []
    for row in cursor:
        location = (row[0])
        locationList.append(location)

    return  locationList


