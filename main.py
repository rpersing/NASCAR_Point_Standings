from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from Driver import Driver

PATH = "D:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://www.nascar.com/standings/nascar-cup-series/")

all_drivers = []
playoffs = []

time.sleep(2)

for i in range(2, 41):
    win = False
    name_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/table/tbody/tr[{}]/td[2]/a/span[2]"
    points_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[2]"
    laps_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[9]"

    try:
        name = driver.find_element_by_xpath(name_element.format(i)).text
        points = driver.find_element_by_xpath(points_element.format(i)).text
        laps = driver.find_element_by_xpath(laps_element.format(i)).text
    except NoSuchElementException:
        continue

    for j in name:
        if j == "*":
            win = True
            name = name[:-1]

    points = int(points)
    d = Driver(name, points, win, laps)
    all_drivers.append(d)
    if i < 18:
        playoffs.append(d)


driver.close()

running = True

while running:
    count = 1
    command = input("What information would you like?: ")

    if command == "playoffs":
        for driver in playoffs:
            print("{}.) ".format(count).ljust(5) + driver.getName().ljust(16) + "|".rjust(2), driver.getPoints(), "|".rjust(2),
                  driver.hasWon().ljust(7), "|", driver.get_laps_led(), "laps led")
            count += 1

    if command == "all":
        for driver in all_drivers:
            print("{}.) ".format(count).ljust(5) + driver.getName().ljust(16) + "|".rjust(2), driver.getPoints(), "|".rjust(2),
                  driver.hasWon().ljust(7), "|", driver.get_laps_led(), "laps led")
            count += 1
