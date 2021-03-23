class Driver:
    def __init__(self, name: str, points: int, won: bool, laps_led: int):
        self.name = name
        self.points = points
        self.won = won
        # self.wins = amount_of_wins
        self.laps_led = laps_led

    def getName(self):
        return self.name

    def getPoints(self):
        return "Points: " + str(self.points)

    def setName(self, n):
        self.name = n

    def setPoints(self, p):
        self.points = p

    def hasWon(self):
        if self.won:
            return "Win"
        else:
            return "No wins"

    def get_laps_led(self):
        return "Laps led: " + str(self.laps_led)

    def set_laps_led(self, laps):
        self.laps_led = laps
