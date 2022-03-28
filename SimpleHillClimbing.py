from collections import defaultdict
class Graph:
    def __init__(self,n,h):
        self.n=n
        self.h=h
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  
    def hillClimb(self,start,goal):
        print('Best First Search : ')
        print("open","close",sep='\t\t\t')
        opened,closed=[],[]
        opened.append(start)
        print(opened, closed, sep='\t\t\t')
        while opened:
            p=opened.pop(0)
            closed.insert(0,p)
            opened.sort(key=lambda x: self.h[x])
            #Goal node
            if p==goal:
                print(opened,closed,sep='\t\t\t')
                print('Goal node found');return
            #Successors Generation
            for v in self.graph[p]:
                if v not in opened and v not in closed:opened.insert(0,v)
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
g.hillClimb(start,goal)

# Sample input: 
'''
12
a 10
b 10
i 8
f 7
d 4
c 2
h 0
k 0
e 5
j 6
g 3
m 0
11
a b
a i
a f
b d
b c
c h
i k
f e
f g
e j
j m
a j
'''
# Sample output: 
'''
Best First Search : 
open            close
['a']           []
['f', 'i', 'b']         ['a']
['g', 'e', 'i', 'b']            ['f', 'a']
['e', 'i', 'b']         ['g', 'f', 'a']
['j', 'i', 'b']         ['e', 'g', 'f', 'a']
['i', 'b']          ['j', 'e', 'g', 'f', 'a']
Goal node found
'''
