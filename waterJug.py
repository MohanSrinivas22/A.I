class WaterJug:
  def __init__(self,bjmax,sjmax,target):
    self.bjmax=bjmax
    self.sjmax=sjmax
    self.goal=target
  def bfs(self):
    print('BFS Approach : ')
    opened,closed=[],[]
    opened.append((0,0))
    print(opened,closed,sep='\t\t\t')
    while opened:
      p=opened.pop(0)
      closed.append(p)
      # Goal State
      if self.goal in p:
        print(opened,closed,sep='\t\t\t')
        print('Goal State is attained');return
      # Rule - 1 fill Small Jug
      if p[1]==0 and (p[0],self.sjmax) not in closed:opened.append((p[0],self.sjmax))
      # Rule - 2 empty Big Jug
      if p[0]==self.bjmax and (0,p[1]) not in closed: opened.append((0,p[1])) 
      # Rule - 3 empty Small Jug to Big Jug
      if p[0]+p[1]<=self.bjmax and (p[0]+p[1],0) not in closed: opened.append((p[0]+p[1],0))
      # Rule - 4 transfer Small Jug to Big Jug
      if p[0]+p[1]>self.bjmax:
        temp=self.bjmax-p[0]
        temp=(p[0]+temp,p[1]-temp)
        if temp not in opened+closed: opened.append(temp)
      # Rule - 5 fill Big Jug
      if p[0]==0 and (self.bjmax,p[1]) not in closed:
          opened.append((self.bjmax,p[1]))
      # Rule - 6 empty Small Jug
      if p[1]==self.sjmax and (p[0],0) not in closed:
          opened.append((p[0],0))
      # Rule - 7 Empty Big Jug to Small Jug
      if p[0]-p[1]>=0 and p[0]-p[1]<=self.sjmax:
        if (p[0]-p[1],p[1]) not in closed:opened.append((p[0]-p[1],p[1]))
      print(opened,closed,sep='\t\t\t')
    print('Goal State not Possible')
  def dfs(self):
    print('DFS Approach : ')
    opened,closed=[],[]
    opened.append((0,0))
    print(opened,closed,sep='\t\t\t')
    while opened:
      p=opened.pop()
      closed.append(p)
      # Goal State
      if self.goal in p:
        print(opened,closed,sep='\t\t\t')
        print('Goal State is attained');return
      # Rule - 1 fill Small Jug
      if p[1]==0 and (p[0],self.sjmax) not in closed:opened.append((p[0],self.sjmax))
      # Rule - 2 empty Big Jug
      if p[0]==self.bjmax and (0,p[1]) not in closed: opened.append((0,p[1])) 
      # Rule - 3 empty Small Jug to Big Jug
      if p[0]+p[1]<=self.bjmax and (p[0]+p[1],0) not in closed: opened.append((p[0]+p[1],0))
      # Rule - 4 transfer Small Jug to Big Jug
      if p[0]+p[1]>self.bjmax:
        temp=self.bjmax-p[0]
        temp=(p[0]+temp,p[1]-temp)
        if temp not in opened+closed: opened.append(temp)
      # Rule - 5 fill Big Jug
      if p[0]==0 and (self.bjmax,p[1]) not in closed:
          opened.append((self.bjmax,p[1]))
      # Rule - 6 empty Small Jug
      if p[1]==self.sjmax and (p[0],0) not in closed:
          opened.append((p[0],0))
      # Rule - 7 Empty Big Jug to Small Jug
      if p[0]-p[1]>=0 and p[0]-p[1]<=self.sjmax:
        if (p[0]-p[1],p[1]) not in closed:opened.append((p[0]-p[1],p[1]))
      print(opened,closed,sep='\t\t\t')
    print('Goal State not Possible')

bjmax,sjmax,target=map(int,input('Enter capacities of jugs and target : ').split())
w=WaterJug(bjmax, sjmax, target)
w.bfs()
w.dfs()
