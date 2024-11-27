colors = [1]
adj = {}
res = {}
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

def safe_color(s):
    for c in colors:
        check = 0
        for i in adj[s]:
            if i in res and res[i] == c:
                check = 1
                break
        if check != 1:
            return c
            
    newc=len(colors) + 1
    colors.append(newc)
    return newc

def dfs(s):
    res[s] = safe_color(s)
    for i in adj[s]:
        if i not in res:
            dfs(i)

dfs(1)
print(res)
