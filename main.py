from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from Driver import Driver

PATH = "D:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.nascar.com/standings/nascar-cup-series/")

topTen = []

time.sleep(2)

for i in range(2, 12):
    win = False
    name = driver.find_element_by_xpath("//*[@id='pgc-160534-1-0']/div[2]/div[2]/table/tbody/tr[{}]/td[2]/a/span[2]"
                                        .format(i)).text
    points = driver.find_element_by_xpath("//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[2]"
                                          .format(i)).text

    for j in name:
        if j == "*":
            win = True
            name = name[:-1]

    points = int(points)
    d = Driver(name, points, win)
    topTen.append(d)

driver.close()

count = 1
for i in topTen:
    print("{}.) ".format(count).ljust(5) + i.getName().ljust(16) + " |", i.getPoints(), "|".rjust(2), i.hasWon().ljust(5))
    count += 1
