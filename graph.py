import pygal
import calculationsForAverages
import calculationsForScatter
import calculationsForAgeGroups
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
def ageGroupPie():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Age group categories (in %)'
    pie_chart.add('Under 20', calculationsForAgeGroups.getAllAgeGroup(0,19))
    pie_chart.add('20-29', calculationsForAgeGroups.getAllAgeGroup(20,29))
    pie_chart.add('30-39', calculationsForAgeGroups.getAllAgeGroup(30,39))
    pie_chart.add('40-49', calculationsForAgeGroups.getAllAgeGroup(40, 49))
    pie_chart.add('50-59', calculationsForAgeGroups.getAllAgeGroup(50, 59))
    pie_chart.add('60-69', calculationsForAgeGroups.getAllAgeGroup(60, 69))
    pie_chart.add('70-79', calculationsForAgeGroups.getAllAgeGroup(70, 79))
    pie_chart.render_to_file('agePie.svg')
ageGroupPie()