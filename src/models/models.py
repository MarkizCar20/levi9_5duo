class PlayerStats:

    valor_index = 0
    eff_fg = 0
    truesht_eff = 0
    holling_as = 0
    points = 0

    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.appearances = 0
        self.ftm = 0
        self.fta = 0
        self.ft_percent = 0
        self.twopm = 0
        self.twopa = 0
        self.twp_percent = 0
        self.threepm = 0
        self.threepa = 0
        self.threep_percent = 0
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
            self.ftm = self.ftm / self.appearances
            self.fta = self.fta / self.appearances
            if (self.fta != 0):
                self.ft_percent = float((self.ftm/self.fta)*100)
            self.twopm = self.twopm / self.appearances
            self.twopa = self.twopa / self.appearances
            if (self.twopa != 0):
                self.twp_percent = float((self.twopm/self.twopa)*100)
            self.threepm = self.threepm / self.appearances
            self.threepa = self.threepa / self.appearances
            if (self.threepa != 0):
                self.threep_percent = float((self.threepm/self.threepa)*100)
            self.reb = self.reb / self.appearances
            self.blk = self.blk / self.appearances
            self.ast = self.ast / self.appearances
            self.stl = self.stl / self.appearances
            self.tov = self.tov / self.appearances
            self.points = (self.twopm*2 + self.threepm*3 + self.ftm*1)
    
    def calculate_advanced(self):
        self.valor_index = (self.ftm + self.twopm*2 + self.threepm*3 + self.reb + self.blk + self.ast + self.stl) - (self.fta - self.ftm + self.twopa - self.twopm + self.threepa - self.threepm + self.tov)
        if (self.twopa != 0 or self.threepa != 0):
            self.eff_fg = 100*(self.twopm + self.threepm + 0.5*self.threepm)/(self.twopa + self.threepa)
        if (self.fta != 0):
            self.truesht_eff = (self.points/(2.0*(self.twopa+self.threepa+0.475*self.fta)))*100
        if (self.tov != 0):
            self.holling_as = (self.ast/(self.twopa+self.threepa+0.475*self.fta+self.ast+self.tov))*100
