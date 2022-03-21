class WaterJug:
    
    def __init__(self,bjmax,sjmax,bj,sj,goal):
        self.bjmax=bjmax
        self.sjmax=sjmax
        self.bj=bj
        self.sj=sj
        self.goal=goal
        
    def bfs(self):
        opened,closed=[],[]
        opened.append((0,0))
        p=(0,0)
        while self.goal not in p:
            p=opened.pop(0)
            closed.append(p)
            bj,sj=p
            #Goal case
            if bj==self.goal or sj==self.goal:
                print(p,' ',opened,' ',closed)
                print("success")
                return
            #Rule - 1 fill bj
            if bj==0 and ((self.bjmax,sj) not in closed) and ((self.bjmax,sj) not in opened):
                opened.append((self.bjmax,sj))
            #Rule - 2 fill sj
            if sj==0 and ((bj,self.sjmax) not in closed) and ((bj,self.sjmax) not in opened):
                opened.append((bj,self.sjmax))
            #Rule - 3 empty bj
            if bj>0 and ((0,sj) not in closed) and ((0,sj) not in opened):
                opened.append((0,sj))    
            #Rule - 4 empty sj
            if sj>0 and ((bj,0) not in closed) and ((bj,0) not in opened):
                opened.append((bj,0))
            #Rule - 5 Transfer from bj to sj
            if bj>0:
                tbj,tsj=bj,sj
                x=min(self.bjmax-sj,bj)
                tsj+=x;tbj-=x
                if ((tbj,tsj) not in closed) and ((tbj,tsj) not in opened):
                    opened.append((tbj,tsj))
                print(p,opened,closed,sep='\t')
                
    def dfs(self):
        opened,closed=[],[]
        opened.append((0,0))
        p=(0,0)
        while self.goal not in p:
            p=opened.pop()
            closed.append(p)
            bj,sj=p
            #Goal case
            if bj==self.goal or sj==self.goal:
                print(p,' ',opened,' ',closed)
                print("success")
                return
            #Rule - 1 fill bj
            if bj==0 and ((self.bjmax,sj) not in opened) and ((self.bjmax,sj) not in closed):
                opened.append((self.bjmax,sj))
            #Rule - 2 fill sj
            if sj==0 and ((bj,self.sjmax) not in closed) and ((bj,self.sjmax) not in opened):
                opened.append((bj,self.sjmax))
            #Rule - 3 empty bj
            if bj>0 and ((0,sj) not in closed) and ((0,sj) not in opened):
                opened.append((0,sj))    
            #Rule - 4 empty sj
            if sj>0 and ((bj,0) not in closed) and ((bj,0) not in opened):
                opened.append((bj,0))
            #Rule - 5 Transfer from bj to sj
            if bj>0:
                tbj,tsj=bj,sj
                x=min(self.bjmax-sj,bj)
                tsj+=x;tbj-=x
                if ((tbj,tsj) not in closed) and ((tbj,tsj) not in opened):
                    opened.append((tbj,tsj))
                print(p,opened,closed,sep='\t')
                
        
w=WaterJug(5,3,0,0,4)
print('current ',' open ',' close',sep='\t')
w.bfs()
print('current ',' open ',' close',sep='\t')
w.dfs()   
