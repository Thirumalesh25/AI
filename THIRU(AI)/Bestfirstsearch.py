from queue import PriorityQueue

def BFS(s,goal):
    v=[s]
    pq=PriorityQueue()
    pq.put((0,s))
    while not pq.empty():
        _,n=pq.get()
        path.append(n)
        
        if n==goal:
            return path
        
        for ch,c in g[n]:
            if ch not in v:
                pq.put((c,ch))
                v.append(ch)
                
    return None

g={}
path=[]
n=int(input("No.of Edges : "))
for _ in range(n):
    x,y,c=map(int, input().split())
    if x not in g:
        g[x]=[]
    if y not in g:
        g[y]=[]
    g[x].append((y,c))
    g[y].append((x,c))
s=int(input("Start : "))
goal=int(input("Goal : "))
if not BFS(s, goal) : print("Not Found")
print(path)
