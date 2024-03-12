
with open("frozen.txt", "r") as file:
    characters = []
    for line in file:
        characters.append(line[:-1])
    
    print(characters)
    

