from collections import defaultdict
class Graph:
  def __init__(self,n,h):
    self.n=n
    self.h=h
    self.graph=defaultdict(list)
    
  def addEdge(self,u,v):
    self.graph[u].append(v)
    self.graph[v].append(u)
  
  def bestfs(self,start,goal):
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
      for v in self.graph[p]:
        if v not in opened and v not in closed:opened.append(v)
      opened.sort(key=lambda x: self.h[x])
      print(opened,closed,sep='\t\t\t')
    print('Goal node not found')

n=int(input('Enter no.of nodes: '))
h={}
for _ in range(n):
  u,i=input('Enter node and it\'s heuristic: ').split()
  h[u]=int(i)
g=Graph(n,h)
m=int(input('Enter no.of edges: '))
for _ in range(m):
  u,v=input('Enter edge nodes: ').split()
  g.addEdge(u,v)
start,goal=input('Enter start and goal states: ').split()
g.bestfs(start,goal)
