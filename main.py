from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from Driver import Driver
from Track import Track

PATH = "D:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
web_driver = webdriver.Chrome(PATH, options=options)
web_driver.get("https://www.nascar.com/standings/nascar-cup-series/")


def get_playoffs():
    for k in range(0, 16):
        print("{}.) ".format(k + 1).ljust(5) + all_drivers[k].getName().ljust(16) + "|".rjust(2) +
              all_drivers[k].getPoints() + "|".rjust(2),
              all_drivers[k].hasWon().ljust(7) + "|" + all_drivers[k].get_laps_led())


def get_all_drivers():
    for count, each in enumerate(all_drivers, start=1):
        print("{}.) ".format(count).ljust(5) + each.getName().ljust(18) + "|".rjust(2),
              each.getPoints() + " | ".ljust(3).rjust(3) + each.hasWon().ljust(8).rjust(8) + " | " +
              each.get_amount_of_wins() + " | " + each.get_laps_led())


def get_winners():
    count = 1
    for w in all_drivers:
        if w.hasWon() == "Win":
            print("{}.) ".format(count).ljust(5) + w.getName() + " | " + w.get_amount_of_wins())
            count += 1


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

playoff_sort = web_driver.find_element_by_xpath(
    "//*[@id=\"pgc-160534-1-0\"]/div[2]/div[2]/div/table/tbody/tr[1]/th[12]")

playoff_sort.click()

for i in range(2, 41):
    won = False
    name_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/table/tbody/tr[{}]/td[2]/a/span[2]"
    points_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[2]"
    laps_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[9]"
    win_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[5]"
    dnf_element = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[8]"
    stage_wins = "//*[@id='pgc-160534-1-0']/div[2]/div[2]/div/table/tbody/tr[{}]/td[10]"

    try:
        name = web_driver.find_element_by_xpath(name_element.format(i)).text
        points = web_driver.find_element_by_xpath(points_element.format(i)).text
        laps = web_driver.find_element_by_xpath(laps_element.format(i)).text
        num_wins = web_driver.find_element_by_xpath(win_element.format(i)).text
        dnf = web_driver.find_element_by_xpath(dnf_element.format(i)).text
        stages = web_driver.find_element_by_xpath(stage_wins.format(i)).text
    except NoSuchElementException:
        continue

    for j in name:
        if j == "*":
            won = True
            name = name[:-1]

    points = int(points)
    d = Driver(name, points, won, num_wins, dnf, stages, laps)
    all_drivers.append(d)

schedule = []
web_driver.get("https://www.nascar.com/nascar-cup-series/2021/schedule/")

t_brand_element = "//*[@id=\"pgc-284644-4-0\"]/div/div[{}]/ul/li[{}]/div/div[2]/h3"
t_name_element = "//*[@id=\"pgc-284644-4-0\"]/div/div[{}]/ul/li[{}]/div/div[2]/p[1]"
t_laps_element = "//*[@id=\"pgc-284644-4-0\"]/div/div[{}]/ul/li[{}]/div[1]/div[3]/p[2]"

for month in range(3, 13):
    for races in range(1, 6):
        try:
            t_brand = web_driver.find_element_by_xpath(t_brand_element.format(month, races)).text
            t_name = web_driver.find_element_by_xpath(t_name_element.format(month, races)).text
            t_laps = web_driver.find_element_by_xpath(t_laps_element.format(month, races)).text
            t_laps = t_laps.split("-")
            t_laps = t_laps[1].strip()
            t_laps = t_laps.split("/")
            t_laps, t_miles = t_laps[0], t_laps[1]

            track = Track(t_brand, t_name, t_laps, t_miles)
            schedule.append(track)
        except NoSuchElementException:
            continue

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
        print("POS | NAME              | POINTS      | HAS WON  | NUM OF WINS       | LAPS LED")
        get_all_drivers()

    if command == "winners":
        get_winners()

    # TODO make specific driver stats more specific with data visualization
    if command == "driver":
        get_specific_driver()

    if command == "help":
        print(command_help)

    if command == "quit":
        print("Goodbye!")
        running = False
