def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pour(j1c, j2c, d):
    j1, j2 = j1c, 0
    steps = [(j1, j2)]
    
    while j1 != d and j2 != d:
        t = min(j1, j2c - j2)
        j2 += t
        j1 -= t
        steps.append((j1, j2))

        if j1 == d or j2 == d:
            break
        if j1 == 0:
            j1 = j1c
            steps.append((j1, j2))
        if j2 == j2c:
            j2 = 0
            steps.append((j1, j2))
    
    return steps

def minSteps(j1c, j2c, d):
    if d > max(j1c, j2c) or d % gcd(j1c, j2c) != 0:
        return []
    steps1 = pour(j1c, j2c, d)
    steps2 = pour(j2c, j1c, d)
    if(len(steps1) <= len(steps2)): print("jug 1, jug 2")
    else: print("jug 2, jug 1")
    return steps1 if len(steps1) <= len(steps2) else steps2

j1c = int(input("Enter jug 1 capacity: "))
j2c = int(input("Enter jug 2 capacity: "))
d = int(input("Enter target volume: "))

r = minSteps(j1c, j2c, d)
if r:
    for i in r:
        print(i)
    print("Steps:" , len(r))
else:
    print("No solution.")
