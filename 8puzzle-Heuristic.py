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
