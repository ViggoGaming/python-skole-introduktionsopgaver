import random

# Tilføj 20 tilfældige tal til listen "tal"
tal = [random.randint(0, 100) for i in range(0, 20)]
print(tal)

# Sortering af listen
tal.sort()
print(tal)

# Byt om på rækkefølgen af tal i listen
tal[0], tal[3] = tal[3], tal[0] 
print(tal)

# Indsæt et element midt i listen
tal.insert(int((len(tal)/2)), 55)
print(tal)

# Tilføjelse af nyt tal
x = int(input("Angiv et tal: "))
tal.append(x)
print(tal)
