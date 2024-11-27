import heapq

def Astar(s, goal):
    ol = [(h[s], s)]
    came_from = {}
    g = {s: 0}

    while ol:
        _, n = heapq.heappop(ol)
        if n == goal:
            path = [n]
            while n in came_from:
                n = came_from[n]
                path.append(n)
            return path[::-1]

        for child, cost in graph[n]:
            new_score = g[n] + cost
            if new_score < g.get(child, float('inf')):
                g[child] = new_score
                heapq.heappush(ol, (new_score + h[child], child))
                came_from[child] = n

    return None

adj = {}
n = int(input("No.of Edges: "))
print("Edges :")
for _ in range(n):
    x, y, c = map(int, input().split())
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append((y, c))
    adj[y].append((x, c))

h = {}
print("Heuristics:")
for _ in range(len(adj)):
    x, a = map(int, input().split())
    h[x] = a

s = int(input("Start node: "))
goal = int(input("Goal node: "))

path = Astar(s, goal)
print("Path:", path if path else "No path found.")
