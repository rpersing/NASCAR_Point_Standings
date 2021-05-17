class Driver:
    def __init__(self, name: str, points: int, won: bool, amount_of_wins: int, dnfs: str, stage_wins: int,
                 laps_led: int):
        self.name = name
        self.points = points
        self.won = won
        self.amount_of_wins = amount_of_wins
        self.dnfs = dnfs
        self.stage_wins = stage_wins
        self.laps_led = laps_led

    def getName(self):
        return self.name

    def setName(self, n):
        self.name = n

    def getPoints(self):
        return str(self.points)

    def setPoints(self, p):
        self.points = p

    def getPlayoffPoints(self):
        return self.playoff_points

    def setPlayoffPoints(self, pp):
        self.playoff_points = pp

    def hasWon(self):
        if self.won:
            return "Win"
        else:
            return "No wins"

    def get_laps_led(self):
        return "Laps led: " + str(self.laps_led)

    def set_laps_led(self, laps):
        self.laps_led = laps

    def get_amount_of_wins(self):
        return "Number of wins: " + str(self.amount_of_wins)

    def set_amount_of_wins(self, a_o_w):
        self.amount_of_wins = a_o_w

    def get_dnfs(self):
        return str(self.dnfs)

    def set_dnfs(self, dnf):
        self.dnfs = dnf

    def get_stage_wins(self):
        return str(self.stage_wins)

    def set_stage_wins(self, sw):
        self.stage_wins = sw
