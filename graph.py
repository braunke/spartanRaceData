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
    locations = calculations.getRaceList()
    line_chart = pygal.Bar()
    line_chart.title = 'Average Times Males vs Female'
    line_chart.x_labels = locations

    line_chart.add('Males', maleRace)
    line_chart.add('Females', femaleRace)
    line_chart.render_to_file('averageMFBar.svg')
averageMvsF()