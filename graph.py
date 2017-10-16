import pygal
import calculationsForAverages
import calculationsForScatter
import calculationsForAgeGroups
import calculationsTopTimes
#used this site for help with pygal
#http://www.pygal.org/en/stable/documentation/types/xy.html#scatter-plot
#graph of average race finish times
def averageTimesGraph():
    races = calculationsForAverages.getItAll()
    line_chart = pygal.HorizontalBar(title='Average race finish times', x_title='Hours')
    for race in races:
        line_chart.add(race[1], race[0])
    line_chart.render_to_file('averageBar.html')
#averageTimesGraph()
def averageMvsF():
    maleRace = calculationsForAverages.getAllMale()
    femaleRace = calculationsForAverages.getAllFemale()
    locations = calculationsForAverages.getRaceList()
    line_chart = pygal.Bar(title='Average Times Males vs Female', x_title='Races', y_title='Hours', x_label_rotation=20)
    line_chart.x_labels = locations
    line_chart.add('Males', maleRace)
    line_chart.add('Females', femaleRace)
    line_chart.render_to_file('averageMFBar.html')
averageMvsF()
def elevationScatter():
    xy_chart = pygal.XY(title='Affects of Elevation', x_title='Hours', y_title='Elevation')
    locations = calculationsForAverages.getRaceList()
    for i in range(0, 10):
        xy_chart.add(locations[i], calculationsForScatter.getItAllAlt(i))
    xy_chart.render_to_file('elevationScatter.html')
elevationScatter()
def ageGroupPie():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Age group categories'
    pie_chart.add('Under 20', calculationsForAgeGroups.getAllAgeGroup(0,19))
    pie_chart.add('20-29', calculationsForAgeGroups.getAllAgeGroup(20,29))
    pie_chart.add('30-39', calculationsForAgeGroups.getAllAgeGroup(30,39))
    pie_chart.add('40-49', calculationsForAgeGroups.getAllAgeGroup(40, 49))
    pie_chart.add('50-59', calculationsForAgeGroups.getAllAgeGroup(50, 59))
    pie_chart.add('60-69', calculationsForAgeGroups.getAllAgeGroup(60, 69))
    pie_chart.add('70-79', calculationsForAgeGroups.getAllAgeGroup(70, 79))
    pie_chart.render_to_file('agePie.html')
ageGroupPie()
def humidityScatter():
    xy_chart = pygal.XY( title='Affects of Humidity', x_title='Hours', y_title='Humidity')
    locations = calculationsForAverages.getRaceList()
    for i in range(0, 10):
        xy_chart.add(locations[i], calculationsForScatter.getItAllHumidity(i))
    xy_chart.render_to_file('humidityScatter.html')
humidityScatter()
def tempScatter():
    xy_chart = pygal.XY(title='Affects of Temperature', x_title='Hours', y_title='Temperature')
    locations = calculationsForAverages.getRaceList()
    for i in range(0, 10):
        xy_chart.add(locations[i], calculationsForScatter.getItAllTemp(i))
    xy_chart.render_to_file('tempScatter.html')
#tempScatter()
def topTimesBar():
    races = calculationsTopTimes.getItAll()
    line_chart = pygal.HorizontalBar(title='Top 20 Average Race Finish Times', x_title='Hours')
    for race in races:
        line_chart.add(race[1], race[0])
    line_chart.render_to_file('topTimesBar.html')
#topTimesBar()
