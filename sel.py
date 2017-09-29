#http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/
# https://stackoverflow.com/questions/41811904/use-an-already-open-webpagewith-selenium-to-beautifulsoup
from selenium import webdriver
from bs4 import BeautifulSoup
pathChrome = '/Users/kayla/Downloads/chromedriver'
browser = webdriver.Chrome(executable_path = pathChrome)
url = 'https://www.spartan.com/en/race/detail/2620/results?fullResults=true'
browser.get(url)
source = browser.page_source
soup = BeautifulSoup(source, "html.parser")
#print (soup.prettify())
result = soup.find_all("tr", class_="result")
columns = ["Name", "Claim", "Bib", "Age", "Gender", "Overall Place", "Gender Place", "Age Group Place", "Time"]
for r in result:
    tds = r.find_all("td")
    colNum = 0
    for td in tds:
        print(columns[colNum] + ": " + td.get_text())
        colNum = colNum + 1
    print("\n")
