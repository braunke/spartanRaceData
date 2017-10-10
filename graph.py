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