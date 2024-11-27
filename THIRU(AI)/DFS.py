adj = {}
n = int(input("No.of Edges: "))
print("Edges:")
for _ in range(n):
    x, y = map(int, input().split())
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append(y)
    adj[y].append(x)

s = int(input("Start node: "))
g = int(input("Goal node: "))

path = []

def dfs(s, g):
    path.append(s)
    if s==g:
        return True
    for i in adj[s]:
        if i not in path:
            if dfs(i, g): return True
    return False
if not dfs(s, g) : print("Not Found")
print(path)
