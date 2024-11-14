from collections import deque
tree = {}

def add(name, parent=None):
    tree.setdefault(name, {"P": parent, "C": []})
    if parent:
        tree.setdefault(parent, {"P": None, "C": []})["C"].append(name)


def inherit(name):
    d = deque([name])  # Initialize BFS queue with the starting node
    k=[]
    while d:
        person = d.popleft()
        k+=[person]
        for child in tree[person]["C"]:
            d.append(child)  # Enqueue child for further exploration
    
    return k if k else "No inheritance found."


def relation(a, b):
    if b in tree[a]["C"]:
        return f"{a} is the parent of {b}."
    
    if a in tree[b]["C"]:
        return f"{a} is the child of {b}."
    
    parent1 = tree[a]["P"]
    parent2 = tree[b]["P"]
    if parent1 == parent2 and parent1 is not None:
        return f"{a} and {b} are siblings."
    
    if b in inherit(a):
        return f"{b} is the desendant of {a}."
        
    if a in inherit(b):
        return f"{a} is the desendant of {b}."
    
    return f"No relationship between {a} and {b}."

while True:
    print("\n--- Family Tree Menu ---")
    print("1. Add Person")
    print("2. Get inheritance")
    print("3. Get relation")
    print("4. Exit")
    ch = input("Choose an option: ")
    
    if ch == "1":
        name = input("Name: ")
        parent = input("Parent(blank): ")
        parent = parent if parent else None
        add(name, parent)
        print(f"{name} added.")
    
    elif ch == "2":
        name = input("Name: ")
        print(f"Descendants of {name}: {inherit(name)}")
    
    elif ch == "3":
        a = input("First person: ")
        b = input("Second person: ")
        print(relation(a, b))
    
    elif ch == "4":
        print("Exiting.")
        break
    
    else:
        print("Invalid choice. Please try again.")
