class PlayerStats:
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.appearances = 0
        self.ftm = 0
        self.fta = 0
        self.twopm = 0
        self.twopa = 0
        self.threepm = 0
        self.threepa = 0
        self.reb = 0
        self.blk = 0
        self.ast = 0
        self.stl = 0
        self.tov = 0

    def add_appearance(self, ftm, fta, twopm, twopa, threepm, threepa, reb, blk, ast, stl, tov):
        self.appearances += 1
        self.ftm += float(ftm)
        self.fta += float(fta)
        self.twopm += float(twopm)
        self.twopa += float(twopa)
        self.threepm += float(threepm)
        self.threepa += float(threepa)
        self.reb += float(reb)
        self.blk += float(blk)
        self.ast += float(ast)
        self.stl += float(stl)
        self.tov += float(tov)

    def calculate_averages(self):
        if self.appearances != 0:
            self.ftm = self.ftm / self.appearances
            self.fta = self.fta / self.appearances
            self.twopm = self.twopm / self.appearances
            self.twopa = self.twopa / self.appearances
            self.threepm = self.threepm / self.appearances
            self.threepa = self.threepa / self.appearances
            self.reb = self.reb / self.appearances
            self.blk = self.blk / self.appearances
            self.ast = self.ast / self.appearances
            self.stl = self.stl / self.appearances
            self.tov = self.tov / self.appearances
        else:
            self.ftm = 0
            self.fta = 0
            self.twopm = 0
            self.twopa = 0
            self.threepm = 0
            self.threepa = 0
            self.reb = 0
            self.blk = 0
            self.ast = 0
            self.stl = 0
            self.tov = 0
