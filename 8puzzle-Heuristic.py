# AStar :
class Graph:
  def __init__(self):
      self.g={}

  def gv(self,node,parent):
    if parent==None:self.g[node]=0;return 0
    if node in self.g:self.g[node]=min(self.g[node],self.g[parent]+1)
    else:self.g[node]=self.g[parent]+1
    return self.g[node]

  def h(self,node):
    count=0
    for i in range(9):
      if node[i]!=self.goal[i]:count+=1
    return count

  def inopen(self,opened,node,parent,g,h):
    for i in opened:
      i=list(i)
      if i[0]==node:
        if i[1]>g+h:
          i[1]=g+h;self.g[i[0]]=self.gv(i[0],parent)
        elif i[1]==g+h and self.g[i[0]]>g:
          self.g[i[0]]=self.gv(i[0],parent);i[1]=g+h
    i=tuple(i)
    
  def aStar(self,start,goal):
    self.goal=goal
    print('aStar Search : ')
    print("open","close",sep='\t\t\t')
    opened,closed=[],[]
    opened.append((start,self.gv(start,None)))
    print(opened, closed, sep='\t\t\t')
    while opened:
      p=opened.pop(0)
      closed.append(p)
      #Goal node
      if self.goal == p[0]:
        print(opened,closed,sep='\t\t\t')
        print('Goal node found');return
      #Successors Generation
      parent=p[0];blank=parent.index(0)
      # Move Up
      if blank>=3:
        v=list(parent)
        v[blank],v[blank-3]=parent[blank-3],parent[blank]
        v=tuple(v);g=self.gv(v,parent);h=self.h(v)
        if (v,g+h) not in opened+closed: opened.append((v,g+h))
        self.inopen(opened,v,parent,g,h)
      # Move Down
      if blank<=5:
        v=list(parent)
        v[blank],v[blank+3]=parent[blank+3],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))    
        self.inopen(opened,v,parent,g,h)  
      # Move Left
      if blank not in (0,3,6):
        v=list(parent)
        v[blank],v[blank-1]=parent[blank-1],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))
        self.inopen(opened,v,parent,g,h)      
      # Move Right
      if blank not in (2,5,8):
        v=list(parent)
        v[blank],v[blank+1]=parent[blank+1],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))
        self.inopen(opened,v,parent,g,h)  
      opened.sort(key=lambda x:x[1])
      print(opened,closed,sep='\t\t\t')
    print('Goal node not found')
    
# Main code :
start=tuple(int(a) for a in input("Enter start state space seperated: ").split())
goal=tuple(int(a) for a in input("Enter goal state space seperated: ").split())
ep=Graph()
ep.aStar(start,goal)




# Best First :
class Graph:
  def __init__(self):
    pass

  def h(self, node):
    count=0
    for i in range(9):
      if node[i]!=self.goal[i]:count+=1
    return count
    
  def bestfs(self,start,goal):
    self.goal=goal
    print('Best First Search : ')
    print("open","close",sep='\t\t\t')
    opened,closed=[],[]
    opened.append(start)
    print(opened, closed, sep='\t\t\t')
    while opened:
      p=opened.pop(0)
      closed.append(p)
      #Goal node
      if p==goal:
        print(opened,closed,sep='\t\t\t')
        print('Goal node found');return
      #Successors Generation
      blank=p.index(0)
      # Move Up
      if blank>=3:
        v=p[:]
        v[blank],v[blank-3]=p[blank-3],p[blank]
        if v not in opened and v not in closed:opened.append(v)
      # Move Down
      if blank<=5:
        v=p[:]
        v[blank],v[blank+3]=p[blank+3],p[blank]
        if v not in opened and v not in closed:opened.append(v)    
      # Move Left
      if blank not in (0,3,6):
        v=p[:]
        v[blank],v[blank-1]=p[blank-1],p[blank]
        if v not in opened and v not in closed:opened.append(v)
      # Move Right
      if blank not in (2,5,8):
        v=p[:]
        v[blank],v[blank+1]=p[blank+1],p[blank]
        if v not in opened and v not in closed:opened.append(v)
      opened.sort(key=lambda x: self.h(x))
      print(opened,closed,sep='\t\t\t')
    print('Goal node not found')

# Main code :
start=[int(a) for a in input("Enter start state space seperated: ").split()]
goal=[int(a) for a in input("Enter goal state space seperated: ").split()]
ep=Graph()
ep.bestfs(start,goal)




# Branch and Bound :
class Graph:
  def __init__(self):
      self.g={}  

  def gv(self,node,parent):
    if parent==None:self.g[node]=0;return 0
    if node in self.g:self.g[node]=min(self.g[node],self.g[parent]+1)
    else:self.g[node]=self.g[parent]+1
    return self.g[node] 
    
  def branch_bounds(self,start,goal):
    self.goal=goal
    print('Branch and bound Search : ')
    print("open","close",sep='\t\t\t')
    opened,closed=[],[]
    opened.append((start,self.gv(start,None)))
    print(opened, closed, sep='\t\t\t')
    while opened:
      p=opened.pop(0)
      closed.append(p)
      #Goal node
      if self.goal == p[0]:
        print(opened,closed,sep='\t\t\t')
        print('Goal node found');return
      #Successors Generation
      parent=p[0];blank=parent.index(0)
      # Move Up
      if blank>=3:
        v=list(parent)
        v[blank],v[blank-3]=parent[blank-3],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))
      # Move Down
      if blank<=5:
        v=list(parent)
        v[blank],v[blank+3]=parent[blank+3],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))    
      # Move Left
      if blank not in (0,3,6):
        v=list(parent)
        v[blank],v[blank-1]=parent[blank-1],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))
      # Move Right
      if blank not in (2,5,8):
        v=list(parent)
        v[blank],v[blank+1]=parent[blank+1],parent[blank]
        v=tuple(v);g=self.gv(v,parent)
        if (v,g) not in opened+closed: opened.append((v,g))
          
      opened.sort(key=lambda x:x[1])
      print(opened,closed,sep='\t\t\t')
    print('Goal node not found')
    
# Main code :
start=tuple(int(a) for a in input("Enter start state space seperated: ").split())
goal=tuple(int(a) for a in input("Enter goal state space seperated: ").split())
ep=Graph()
ep.branch_bounds(start,goal)




# Hill Climbing :
class Graph:
  def __init__(self):pass
    
  def h(self, node):
    count=0
    for i in range(9):
      if node[i]!=self.goal[i]:count+=1
    return count
  
  def hillClimb(self,start,goal):
    self.goal=goal
    print('Hill Climbing Search : ')
    print("open","close",sep='\t\t\t')
    opened,closed=[],[]
    opened.append(start)
    print(opened, closed, sep='\t\t\t')
    while opened:
      p=opened.pop(0)
      closed.insert(0,p)
      opened.sort(key=lambda x: self.h(x))
      #Goal node
      if p==goal:
        print(opened,closed,sep='\t\t\t')
        print('Goal node found');return
      #Successors Generation
      blank=p.index(0)
      # Move Up
      if blank>=3:
        v=list(p[:])
        v[blank],v[blank-3]=p[blank-3],p[blank]
        v=tuple(v)
        if v not in opened and v not in closed:opened.append(v)
      # Move Down
      if blank<=5:
        v=list(p[:])
        v[blank],v[blank+3]=p[blank+3],p[blank]
        v=tuple(v)
        if v not in opened and v not in closed:opened.append(v)    
      # Move Left
      if blank not in (0,3,6):
        v=list(p[:])
        v[blank],v[blank-1]=p[blank-1],p[blank]
        v=tuple(v)
        if v not in opened and v not in closed:opened.append(v)
      # Move Right
      if blank not in (2,5,8):
        v=list(p[:])
        v[blank],v[blank+1]=p[blank+1],p[blank]
        v=tuple(v)
        if v not in opened and v not in closed:opened.append(v)
      print(opened,closed,sep='\t\t\t')
    print('Goal node not found')

# Main code :
start=tuple(int(a) for a in input("Enter start state space seperated: ").split())
goal=tuple(int(a) for a in input("Enter goal state space seperated: ").split())
ep=Graph()
ep.hillClimb(start,goal)




# Beam
class Graph:
  def __init__(self, w):
    self.w=w

  def h(self, node):
    count=0
    for i in range(9):
      if node[i]!=self.goal[i]:count+=1
    return count

  def succs(self, p, opened, closed):
    blank=p.index(0)
    # Move Up
    if blank>=3:
      v=list(p[:])
      v[blank],v[blank-3]=p[blank-3],p[blank]
      v=tuple(v)
      if v not in closed: opened.append(v)
    # Move Down
    if blank<=5:
      v=list(p[:])
      v[blank],v[blank+3]=p[blank+3],p[blank]
      v=tuple(v)
      if v not in closed:opened.append(v)    
    # Move Left
    if blank not in (0,3,6):
      v=list(p[:])
      v[blank],v[blank-1]=p[blank-1],p[blank]
      v=tuple(v)
      if v not in closed:opened.append(v)
    # Move Right
    if blank not in (2,5,8):
      v=list(p[:])
      v[blank],v[blank+1]=p[blank+1],p[blank]
      v=tuple(v)
      if v not in closed:opened.append(v)
    
  
  def beams(self, start, goal):
    self.goal=goal
    not_found=True
    w_opened,opened,closed=[],[],[]
    if start==self.goal:print("Goal node found");not_found=False;return
    closed.append(start)
    print(opened,w_opened,closed)
    self.succs(start,opened,closed)
    opened.sort(key=lambda x:self.h(x))
    w_opened=opened[:self.w]
    print(opened,w_opened,closed)
    while not_found:
      opened.clear()
      while w_opened:
        p=w_opened.pop(0)
        closed.append(p)
        if p==goal:print(opened,w_opened,closed);print('Goal node found');not_found=False;return
        self.succs(p,opened,closed)
      opened.sort(key=lambda x:self.h(x))
      w_opened=opened[:self.w]  
      print(opened,w_opened,closed)
      if all(i in closed for i in w_opened):print('Goal node not found');return

# Main code :
start=tuple(int(a) for a in input("Enter start state space seperated: ").split())
goal=tuple(int(a) for a in input("Enter goal state space seperated: ").split())
ep=Graph(2)
ep.beams(start,goal)
