import pygal
import calculations
def averageTimesGraph():
    races = calculations.getItAll()
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Average race finish times'
    for race in races:
        line_chart.add(race[1], race[0])
    line_chart.render_to_file('averageBar.svg')
averageTimesGraph()
def averageMvsF():
    maleRace = calculations.getAllMale()
    femaleRace = calculations.getAllFemale()
    line_chart = pygal.Bar()
    line_chart.title = 'Average TImes Males vs Female'
    line_chart.x_labels = map(str, range(2002, 2013))
    for mRace in maleRace:
        line_chart.add(mRace[1], mRace[0])
    for fRace in femaleRace:
        line_chart.add(fRace[1], fRace[0])
    line_chart.render()
averageMvsF()