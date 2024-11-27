from collections import deque
tree = {}
died = []  

def add(name, parent=None):
    tree.setdefault(name, {"P": parent, "C": []})
    if parent:
        tree.setdefault(parent, {"P": None, "C": []})["C"].append(name)

def inherit(name):
    d = deque([name])  
    k = []
    while d:
        person = d.popleft()
        if person not in died:  
            k.append(person)
        for child in tree[person]["C"]:
            d.append(child)
    return k if k else "No inheritance found."
    
def death(name):
    if name not in tree:
        print(f"{name} does not exist.")  
        return
    died.append(name) 

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
    print("3. Death")
    print("4. Get relation")
    print("5. Exit")
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
        name = input("Name: ")  
        death(name) 
        print(f"{name} marked as deceased.")
    
    elif ch == "4":
        a = input("First person: ")
        b = input("Second person: ")
        print(relation(a, b))
    
    elif ch == "5":
        print("Exiting.")
        break
    
    else:
        print("Invalid choice. Please try again.")
