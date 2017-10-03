#http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/
# https://stackoverflow.com/questions/41811904/use-an-already-open-webpagewith-selenium-to-beautifulsoup
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import database
import json

pathChrome = '/Users/kayla/Downloads/chromedriver'
with open('races.json') as data_file:
    data = json.load(data_file)
browser = webdriver.Chrome(executable_path = pathChrome)

database.createDatabase()
for race in data["races"] :
    url = race["resultsURL"]
    elevation = race["elevation"]
    humidity = race["humidity"]
    temperature = race["temperature"]
    location = race["name"]
    raceID = database.createRace(location, elevation, temperature, humidity)

    browser.get(url)
    time.sleep(2)
    resultNum = 0
    while True:
        source = browser.page_source
        soup = BeautifulSoup(source, "html.parser")
        curSpanList = browser.find_elements_by_css_selector("div[class=pagination] span.active")
        if len(curSpanList) > 0:
            curPage = curSpanList[0].text
        else:
            curPage = "Last"
        print("scraping page: " + curPage)
        result = soup.find_all("tr", {"class":["result"]})
        #columns = ["Name", "Claim", "Bib", "Age", "Gender", "Overall Place", "Gender Place", "Age Group Place", "Time"]
        for r in result:
            tds = r.find_all("td")
            if (len(tds) == 9):
                index = 0
                resultString = ""
                for td in tds:
                    text = td.get_text()
                    formatedtext = text + " "
                    if index ==3 or index == 4  or index ==8:
                        resultString += formatedtext
                    index += 1
                resultNum += 1
                database.addRows(resultString, raceID)
        if "Last" in curPage:
            print("Scraped " + str(resultNum) + " results.")
            break
        nextSpanList = browser.find_elements_by_css_selector("div[class=pagination] span.active + span")
        if len(nextSpanList) > 0:
            button = nextSpanList[0]
            button.click()
            nextSpanList = browser.find_elements_by_css_selector("div[class=pagination] span.active")
            if len(nextSpanList) > 0:
                nextPage = nextSpanList[0].text
                if curPage == nextPage:
                    button = browser.find_elements_by_css_selector("div[class=pagination] span.active + span")[0]
                    button.click()
        time.sleep(2)
database.displayRows()