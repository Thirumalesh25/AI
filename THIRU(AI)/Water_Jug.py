def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pour(m, n, d):
    j1, j2 = m, 0
    steps = [(j1, j2)]
    
    while j1 != d and j2 != d:
        t = min(j1, n - j2)
        j2 += t
        j1 -= t
        steps.append((j1, j2))

        if j1 == d or j2 == d:
            break
        if j1 == 0:
            j1 = m
            steps.append((j1, j2))
        if j2 == n:
            j2 = 0
            steps.append((j1, j2))
    
    return steps

def minSteps(m, n, d):
    if d > max(m, n) or d % gcd(m, n) != 0:
        return []
    steps1 = pour(m, n, d)
    steps2 = pour(n, m, d)
    if(len(steps1) <= len(steps2)): print("jug 1, jug 2")
    else: print("jug 2, jug 1")
    return steps1 if len(steps1) <= len(steps2) else steps2

m = int(input("Enter jug 1 capacity: "))
n = int(input("Enter jug 2 capacity: "))
d = int(input("Enter target volume: "))

r = minSteps(m, n, d)
if r:
    for i in r:
        print(i)
    print("Steps:" , len(r))
else:
    print("No solution.")
