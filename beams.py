from collections import defaultdict
class Graph:
    def __init__(self, n, w, h):
        self.graph=defaultdict(list) 
        self.n=n
        self.w=w
        self.h=h

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def beams(self, start, goal):
        not_found=True
        if goal not in self.h:print('Goal node not found');return
        w_opened,opened,closed=[],[],[]
        if start==goal:print("Goal node found");not_found=False;return
        closed.append(start)
        print(opened,w_opened,closed)
        for i in self.graph[start]:
            opened.append(i)
        opened.sort(key=lambda x:self.h[x])
        w_opened=opened[:self.w]
        print(opened,w_opened,closed)
        while not_found:
            opened.clear()
            while w_opened:
                p=w_opened.pop(0)
                closed.append(p)
                if p==goal:print(opened,w_opened,closed);print('Goal node found');not_found=False;return
                for v in self.graph[p]:
                    if v not in closed:opened.append(v)
            opened.sort(key=lambda x:self.h[x])
            w_opened=opened[:self.w]  
            print(opened,w_opened,closed)
            if all(i in closed for i in w_opened):print('Goal node not found');return

n=int(input("Enter no.of nodes : "))
w=int(input("Enter w : "))
h={}
for _ in range(n):
    u,i=input('Enter node and it\'s heuristic : ').split()
    h[u]=int(i)
g=Graph(n,w,h)
m=int(input('Enter no.of Edges : '))
for _ in range(m):
    u,v=input('Enter edge nodes : ').split()
    g.addEdge(u,v)
start,goal=input('Enter start and goal nodes : ').split()
g.beams(start,goal)


#Sample input:
'''
17
2
a 20
b 10
c 13
d 9
e 7
f 11
g 8
h 9
i 4
j 12
k 9
l 5
m 7
n 10
p 14
q 3
r 9
17
a b
a c
a d
b e
b f
c g
d h
d i
d j
e k
e l
f m
g n
h o
i p
i q
j r
a q
'''
#Sample Output: 
'''
[] [] ['a']
['d', 'b', 'c'] ['d', 'b'] ['a']
['i', 'e', 'h', 'f', 'j'] ['i', 'e'] ['a', 'd', 'b']
['q', 'l', 'k', 'p'] ['q', 'l'] ['a', 'd', 'b', 'i', 'e']
[] ['l'] ['a', 'd', 'b', 'i', 'e', 'q']
Goal node found
'''
