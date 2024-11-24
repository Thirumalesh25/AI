from collections import deque
tree = {}

def add(name, parent=None):
    tree.setdefault(name, {"P": parent, "C": []})
    if parent:
        tree.setdefault(parent, {"P": None, "C": []})["C"].append(name)


def inherit(name):
    d = deque([name])  
    k=[]
    while d:
        person = d.popleft()
        k+=[person]
        for child in tree[person]["C"]:
            d.append(child) 
    
    return k if k else "No inheritance found."


while True:
    print("\n--- Family Tree Menu ---")
    print("1. Add Person")
    print("2. Get inheritance")
    print("3. Exit")
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
        print("Exiting.")
        break
    
    else:
        print("Invalid choice. Please try again.")