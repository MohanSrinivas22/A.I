from collections import defaultdict
def find_all_parents(G, s):
    Q=[s]
    parents = defaultdict(set)
    while len(Q):
        v = Q.pop(0)
        for w in G[v]:
            parents[w].add(v)
            Q.append(w)
    return parents
def find_all_paths(parents, a, b):
    return [a] if a == b else [y+b for x in list(parents[b]) for y in
find_all_paths(parents, a, x)]
def func(x,y):
    l=[(0,y),(x,0),(m,y),(x,n)]
    if (x+y)<=m and y>0:l.append((x+y,0))
    if (x+y)<=n and x>0:l.append((0,x+y))
    if (x+y)>=m and y>0:l.append((m,y-(m-x)))
    if (x+y)>=n and x>0:l.append((x-(n-y),n))
    return list(set(l))
cp,cl,k=[],[],[]
m,n=map(int,input().split())
res1,res2=map(int,input().split())
G={}
cp.append((0,0))
cl.append((0,0))
while cp:
    q=cp.pop(0)
    s=func(q[0],q[1])
    G[q]=[]
    for i in s:
        if i not in cl:
            G[q].append(i)
    for i in s:
        if i not in cl:
            cl.append(i)
            cp.append(i)
            if i==(res1,res2):
                break
print("The path in BFS is:",end=" ")
for i in find_all_paths(find_all_parents(G, (0,0)), (0,0), (res1,res2)):
     for j in range(0,len(i),2):
            print(f"({i[j]},{i[j+1]})",end=" ")
