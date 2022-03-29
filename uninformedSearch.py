'''BFS and DFS'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.g=defaultdict(list)
        
    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)
        
    def bfs(self,start,goal):
        opened,closed=[start],[]
        while opened:
            p=opened.pop(0)
            closed.append(p)
            if p==goal:print('Goal node found');return closed
            for j in self.g[p]:
                if j not in opened and j not in closed:opened.append(j)
        print('Goal node not found');return closed
    
    def dfs(self,start,goal):
        opened,closed=[start],[]
        while opened:
            p=opened.pop(0)
            closed.append(p)
            if p==goal:print('Goal node found');return closed
            c=0
            for j in self.g[p]:
                if j not in opened and j not in closed:opened.insert(c,j);c+=1  
        print('Goal node not found');return closed
    
g=Graph()
n=int(input("Enter no.of Edges: "))
for _ in range(n):
    u,v=input("Enter u v :").split()
    g.addEdge(u,v)
start,goal=input('Start node: '),input('Goal node: ')
bfs_path=g.bfs(start,goal)
dfs_path=g.dfs(start,goal)
print(bfs_path)
print(dfs_path)




'''DFID'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.g=defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append([v,0])
        self.g[v].append([u,0])
    def dfs(self, start, goal, i):
        opened,closed=[],[]
        opened.append([start,0])
        while opened:
            u,v=opened.pop()
            closed.append(u)
            if u==goal:print(u,' ',opened,' ', closed);return 1
            if v<i :
                for j in self.g[u]:
                    j[1]=v+1
                    if j[0] not in closed:opened.append(j)
            print(u,' ',opened,' ', closed)
        return 0
    def dfid(self, start, goal):
        i=x=0
        while x!=1:
            print('DFID with depth = ',i)
            x=self.dfs(start, goal, i)
            i+=1
        print('Goal found')
g=Graph()
n=int(input('No.of edges : '))
for _ in range(n):                              # Enter  Space seperated edge nodes
    u,v=input('Enter Edge nodes : ').split()
    g.addEdge(u,v)
start,goal=input('Enter start and goal nodes : ').split()
g.dfid(start,goal)




''' Bidirectional '''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bds(self, start, goal):
        fopen,bopen,fclose,bclose=[],[],[],[]
        fopen.append(start)
        bopen.append(goal)
        print(fopen,bopen,fclose,bclose,sep='\t\t')
        while fopen and bopen:
            p=fopen.pop(0)
            q=bopen.pop(0)
            if p==q:print('Goal node found');return
            if p not in fclose:fclose.append(p)
            if q not in bclose:bclose.insert(0,q)
            # Generate Succesors :-
            for v in self.graph[p]:
                if v not in fclose:fopen.append(v)
            for v in self.graph[q]:
                if v not in bclose:bopen.append(v)
            print(fopen,bopen,fclose,bclose,sep='\t\t')
            # Goal Case :-
            for i in fopen:
                if i in bopen:print('Goal node found');return
        print('Goal node not found')
        
n=int(input('Enter no.of nodes : '))
m=int(input('Enter no.of edges : '))
g=Graph()
for _ in range(m):
    u,v=input('Enter edge nodes : ').split()
    g.addEdge(u,v)
start, goal=input('Enter start and goal nodes : ').split()
g.bds(start, goal)
