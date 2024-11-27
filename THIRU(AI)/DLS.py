adj = {}
n = int(input("No. of Edges: "))
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
dl= int(input("Enter depth limit: "))

path = []

def dls(s, g, dl):
    path.append(s)
    if s == g:
        return True
    if dl <= 0:
        return False
    for i in adj[s]:
        if i not in path:
            if dls(i, g, dl - 1):
                return True
    return False

if not dls(s, g, dl):
    print("Not Found")
print("Path:", path)
