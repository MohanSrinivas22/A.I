from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(dict)
        self.h=defaultdict(lambda : 0)
    def add_edge(self,u,v,w):
        self.graph[u][v]=w
        self.graph[v][u]=w
    def add_h(self,u,h):
        self.h[u]=h
    def in_Open(self,Open,i,p,d):
        print("inside open")
        if(Open[i][0]>d+self.graph[p][i]+self.h[i]):
            Open[i][2]=p
            Open[i][0]=d+self.graph[p][i]+self.h[i]
            Open[i][3]=d+self.graph[p][i]
    def in_close(self,close,Open,i,p,d):
        print("inside close")
        if(close[i][1]>d+self.graph[p][i]+self.h[i]):
            x=close[i][1]-(d+self.graph[p][i]+self.h[i])
            close[i][0]=p
            close[i][1]=d+self.graph[p][i]+self.h[i]
            d_open,d_close=[[i,d+self.graph[p][i]]],[p,i]
            print(d_open)
            while(d_open):
                print("inside d_open loop")
                element,d=d_open.pop()
                for s in self.graph[element]:
                    if s not in d_close:
                        if s in Open:
                            if(Open[s][0]>d+self.graph[element][s]+self.h[s]):
                                Open[s][0]=d+self.graph[element][s]+self.h[s]
                                Open[s][3]=d+self.graph[element][s]
                                d_open.append([s,d+self.graph[element][s]])
                        elif(s in close):
                            if(close[s][1]>d+self.graph[element][s]+self.h[s]):
                                close[s][1]-=x
                                d_open.append([s,d+self.graph[element][s]])
                        else:
                            pass
                        d_close.append(s)
                print(element,d_open,d_close)
    def A_star(self,start,goal):
        Open,close={start:[self.h[start],start,-1,0]},{}
        p=start
        while(Open):
            Open=list(Open.items())
            p,arr=Open.pop(0)
            f,p,parent,d=arr
            Open=dict(Open)
            close[p]=[parent,f]
            if(p==goal):
                print(p,'        ',Open,'          ',close)
                print('Goal Node found')
                return
            ###print(type(p),type(self.graph[p]))
            for i in self.graph[p]:
                if parent!=i:
                    if i in Open:
                        print("parent is ",p,"child is ",i," in Open")
                        self.in_Open(Open,i,p,d)
                    if i in close:
                        print("parent is ",p,"child is ",i," in close")
                        self.in_close(close,Open,i,p,d)
                    if i not in Open and i not in close:
                        Open[i]=[d+self.graph[p][i]+self.h[i] , i , p , d+self.graph[p][i]]
            Open=dict(sorted(Open.items(), key =lambda kv:(kv[1], kv[0])))
            print(p,'        ',Open,'          ',close)
g=Graph()
n=input('enter edges and their weights separated by coma  : ').split(',')
for i in n:
    u,v,w=map(int,i.split())
    g.add_edge(u,v,w)
print(list(g.graph.items()))
start,goal=map(int,input('enter start,goal').split())
for i in g.graph:
    g.add_h(i,int(input('enter heuristic of node '+str(i)+' : ')))
g.add_h(goal,0)

g.A_star(start,goal)
