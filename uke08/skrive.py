
with open("numbers.txt", "a") as file:

    for i in range(10):
        file.write(str(i) + "\n")

    