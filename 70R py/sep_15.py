dicts = []  
n = int(input("How many dictionaries do you want to insert? "))
for i in range(n):
    print(f"\nDictionary {i+1}:")
    d = {}   
    items = int(input("How many key-value pairs in this dictionary? "))
    for j in range(items):
        key = input(f"Enter key {j+1}: ")
        value = input(f"Enter value for '{key}': ")
        d[key] = value
    dicts.append(d)  
print("\nFinal List of Dictionaries:")
print(dicts)
