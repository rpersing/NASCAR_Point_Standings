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


def get_list_info(section: str):
    if section == "playoffs":
        for k in range(0, 16):
            print("{}.) ".format(k + 1).ljust(5) + all_drivers[k].getName().ljust(16) + "|".rjust(2),
                  all_drivers[k].getPoints(), "|".rjust(2),
                  all_drivers[k].hasWon().ljust(7), "|", all_drivers[k].get_laps_led())
    elif section == "all":
        for count, each in enumerate(all_drivers, start=1):
            print("{}.) ".format(count).ljust(5) + each.getName().ljust(18) + "|".rjust(2),
                  each.getPoints(), " |".ljust(2).rjust(2), each.hasWon().ljust(7).rjust(7), "|", each.get_laps_led())

    elif section == "driver":
        input_driver = input("Which driver would you like to get stats for?: ")
        for n in all_drivers:
            if n.getName().lower() == input_driver.lower():
                return print(n.getName() + "\n" + n.getPoints() + "\n" + n.hasWon() + "\n" + n.get_laps_led())

        return print(input_driver + " does not exist. Please try again.")


all_drivers = []

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

    # print(laps)
    for j in name:
        if j == "*":
            win = True
            name = name[:-1]

    points = int(points)
    d = Driver(name, points, win, laps)
    all_drivers.append(d)


driver.close()

running = True

command_help = "Commands:\n" \
               "playoffs - shows stats of drivers in playoffs\n" \
               "all - shows all drivers stats\n" \
               "driver - get stats for a specific driver\n" \
               "help - reprint all commands"

print(command_help)

while running:

    command = input("What information would you like?: ")

    if command == "playoffs":
        get_list_info(command)

    if command == "all":
        get_list_info(command)

    if command == "driver":
        get_list_info(command)

    if command == "help":
        print(command_help)
