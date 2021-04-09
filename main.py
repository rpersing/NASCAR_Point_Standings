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


def get_playoffs():
    for k in range(0, 16):
        print("{}.) ".format(k + 1).ljust(5) + all_drivers[k].getName().ljust(16) + "|".rjust(2) +
              all_drivers[k].getPoints() + "|".rjust(2),
              all_drivers[k].hasWon().ljust(7) + "|" + all_drivers[k].get_laps_led())


def get_all_drivers():
    for count, each in enumerate(all_drivers, start=1):
        print("{}.) ".format(count).ljust(5) + each.getName().ljust(18) + "|".rjust(2),
              each.getPoints() + " | ".ljust(2).rjust(2) + each.hasWon().ljust(7).rjust(7) + " | " + each.get_laps_led())


def get_winners():
    for enum, w in enumerate(all_drivers):
        if w.hasWon() == "Win":
            print("{}.) ".format(enum).ljust(5) + w.getName())


def get_specific_driver():
    driver_name = input("Which driver would you like to get stats for?: ")
    print("\n-------------------------\n")
    for n in all_drivers:
        if n.getName().lower() == driver_name.lower():
            return print(n.getName() + "\n" + n.getPoints() + "\n" + n.hasWon() + "\n" + n.get_laps_led() + "\n" +
                         n.get_amount_of_wins() + "\nDNFs: " + n.get_dnfs() + "\nStage Wins: " + n.get_stage_wins()
                         + "\n")

    return print(driver_name + " does not exist. Please try again.\n")


all_drivers = []

time.sleep(2)

for i in range(2, 41):
    won = False
    name_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/table/tbody/tr[{}]/td[2]/a/span[2]"
    points_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[2]"
    laps_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[9]"
    win_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[5]"
    dnf_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[8]"
    stage_wins = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[10]"

    try:
        name = driver.find_element_by_xpath(name_element.format(i)).text
        points = driver.find_element_by_xpath(points_element.format(i)).text
        laps = driver.find_element_by_xpath(laps_element.format(i)).text
        num_wins = driver.find_element_by_xpath(win_element.format(i)).text
        dnf = driver.find_element_by_xpath(dnf_element.format(i)).text
        stages = driver.find_element_by_xpath(stage_wins.format(i)).text
    except NoSuchElementException:
        continue

    for j in name:
        if j == "*":
            won = True
            name = name[:-1]

    points = int(points)
    d = Driver(name, points, won, num_wins, dnf, stages, laps)
    all_drivers.append(d)

driver.close()

running = True

command_help = "Commands:\n" \
               "playoffs - shows stats of drivers in playoffs\n" \
               "all - shows all drivers stats\n" \
               "driver - get stats for a specific driver\n" \
               "winners - get names of all drivers that have won\n" \
               "help - reprint all commands\n" \
               "quit - exit the program"

print(command_help)

while running:

    command = input("What information would you like?: \n")

    if command == "playoffs":
        get_playoffs()

    if command == "all":
        get_all_drivers()

    if command == "winners":
        get_winners()

    # TODO make specific driver stats more specific (epic data visualization)
    if command == "driver":
        get_specific_driver()

    if command == "help":
        print(command_help)

    if command == "quit":
        print("Goodbye!")
        running = False

