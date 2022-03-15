from collections import defaultdict
class Graph:
    def __init__(self, n):
        self.graph=defaultdict(list)
        self.n=n
        self.ans=[]
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start, goal):
        visited=[False]*self.n
        queue=[start]
        ans=[]
        flag=False
        while queue:
            print(queue)
            x=queue.pop(0)
            ans.append(x)
            visited[x]=True
            for v in self.graph[x]:
                if visited[v]==False and v not in queue:queue.append(v)
                if v==goal:flag=True;break
            if flag:ans.extend(queue);break
        if flag:print('Goal node is found.')
        else:print('Goal node is not found.')
        return ans
    
    def dfsmain(self,start,goal):
        if start==goal:return True
        self.vis.add(start)
        self.anss.append(start)
        flag=False
        for v in self.graph[start]:
            if v==goal:flag=True;break
            if v not in self.vis:self.dfsmain(v, self.vis)
        return flag
    
    def dfs(self, start, goal):
        self.vis=set()
        self.anss=[]
        if self.dfsmain(start, goal):print('Goal node is found.')
        else:print('Goal node is not found.')
        return self.anss

if __name__=='__main__':
    g=Graph(int(input('No.of Nodes: ')))
    for _ in range(int(input("Enter no.of edges: "))):
        p,c=input('Enter edges: ').split()
        g.addEdge(int(p),int(c))  
    print(g.bfs(int(input('start node: ')),int(input('goal node: '))))
    print(g.dfs(int(input('start node: ')),int(input('goal node: '))))
