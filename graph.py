import pygal
import calculations
races = calculations.getItAll()

line_chart = pygal.HorizontalBar()
line_chart.title = 'Browser usage in February 2012 (in %)'
for race in races:
    line_chart.add(race[1], race[0])

line_chart.render_to_file('bar_chart.svg')
