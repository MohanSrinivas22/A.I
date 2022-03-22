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
n=int(input())
for _ in range(n):
    u,v=input().split()
    g.addEdge(u,v)
start,goal=input().split()
g.dfid(start,goal)
