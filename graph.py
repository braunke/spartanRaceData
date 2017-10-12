import pygal
import calculationsForAverages
import calculationsForScatter
#used this site for help with pygal
#http://www.pygal.org/en/stable/documentation/types/xy.html#scatter-plot
def averageTimesGraph():
    races = calculationsForAverages.getItAll()
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Average race finish times'
    for race in races:
        line_chart.add(race[1], race[0])
    line_chart.render_to_file('averageBar.svg')
averageTimesGraph()
def averageMvsF():
    maleRace = calculationsForAverages.getAllMale()
    femaleRace = calculationsForAverages.getAllFemale()
    locations = calculationsForAverages.getRaceList()
    line_chart = pygal.Bar()
    line_chart.title = 'Average Times Males vs Female'
    line_chart.x_labels = locations

    line_chart.add('Males', maleRace)
    line_chart.add('Females', femaleRace)
    line_chart.render_to_file('averageMFBar.svg')
averageMvsF()
def elevationScatter():
    xy_chart = pygal.XY(stroke=False)
    races = calculationsForScatter.getItAll()
    xy_chart.title = 'Affects of Elevation'
    xy_chart.add('A', races)
    xy_chart.render_to_file('elevationScatter.svg')
elevationScatter()