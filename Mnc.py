class MNC:
    
    def __init__(self,lm,lc,lb,rm,rc,rb,bc,n):
        self.lm=lm
        self.lc=lc
        self.lb=lb
        self.rm=rm
        self.rb=rb
        self.rc=rc
        self.bc=bc
        self.goal=((0,0,0),(n,n,1))
        
    def bfs(self):
        opened,closed=[],[]
        opened.append(((3,3,1),(0,0,0)))
        while opened:
            p=opened.pop(0)
            closed.append(p)
            #Goal case
            if p==self.goal:
                print(p,' ',opened,' ',closed)
                print("success")
                return
            #Rule - 1 2m to right
            if self.lb==1:
                if self.lm-2>=0 and self.lc<=self.lm-2 and self.rc<=self.rm+2 and self.rm+2<=3:
                    temp=((self.lm-2,self.lc,0),(selfrm+2,self.rc,1))
                    if temp not in opened and temp not in closed:
                        opened.append(temp)
                        
            
              #Rule - 2 1m 1c 
                  if self.lm-1>=0 and self.lc-=1>=0 and self.
            

n=int(input('Enter n'))
w=MNC(n,n,1,0,0,0,n)
print('current ',' open ',' close',sep='\t')
w.bfs()
#print('current ',' open ',' close',sep='\t')
#w.dfs()   
