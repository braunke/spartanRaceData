#http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/
# https://stackoverflow.com/questions/41811904/use-an-already-open-webpagewith-selenium-to-beautifulsoup
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import database
pathChrome = '/Users/kayla/Downloads/chromedriver'
browser = webdriver.Chrome(executable_path = pathChrome)
url = 'https://www.spartan.com/en/race/detail/2620/results?fullResults=true'
browser.get(url)
time.sleep(2)
for blerp in range(4):
    source = browser.page_source
    soup = BeautifulSoup(source, "html.parser")
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
                index = index + 1

            database.addRows(resultString)
            print("\n")
    button = browser.find_elements_by_css_selector("div[class=pagination] span.active + span")[0]
    button.click()
    time.sleep(2)