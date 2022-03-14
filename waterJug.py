class Waterjug:
    def __init__(self,bjmax,sjmax,bj,sj,goal):
        self.bjmax=bjmax
        self.sjmax=sjmax
        self.bj=bj
        self.sj=sj
        self.goal=goal
        
    def fillbj(self):
        self.bj=self.bjmax
        print("(",self.bj,",",self.sj,")")
        
    def fillsj(self):
        self.bj=self.bjmax
        print("(",self.bj,",",self.sj,")")
        
    def emptybj(self):
        self.bj=0
        print("(",self.bj,",",self.sj,")")
        
    def emptysj(self):
        self.sj=0
        print("(",self.bj,",",self.sj,")")
        
    def transfer_bj_to_sj(self):
        while True:
            self.bj=self.bj-1
            self.sj=self.sj+1
            if self.bj==0 or self.sj==self.sjmax:
                break
        print("(",self.bj,",",self.sj,")")
        
    def measure_goal(self):
        print("(",self.bj,",",self.sj,")")
        while(True):
            if self.bj==self.goal or self.sj==self.goal:
                print("Successful measuring")
                break
            if self.bj==0:
                self.fillbj()
            elif self.bj>0 and self.sj<self.sjmax:
                self.transfer_bj_to_sj()
            elif self.bj>0 and self.sj==self.sjmax:
                self.emptysj()                
                
if __name__ =='__main__':        
    waterjug=Waterjug(int(input()),int(input()),int(input()),int(input()),int(input()))
    waterjug.measure_goal()
