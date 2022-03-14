class Water_Jug:
    def __init__(self,bj_max,sj_max,bj,sj,goal):
        self.bj_max=bj_max
        self.sj_max=sj_max
        self.bj=bj
        self.sj=sj
        self.goal=goal
    def fill_bj(self):
        self.bj=self.bjmax
        print("(",self.bj,",",self.sj,")")
    def fill_sj(self):
        self.bj=self.bjmax
    def empty_bj(self):
        self.bj=0
    def empty_sj(self):
        self.sj=0
    def pour_bj_to_sj(self):
        x=min(self.sj_max-self.sj,self.)
