names = []
with open("names.txt", "r") as file:
    #Create into an array
    for line in file:
        names.append(list(line.split(",")))
names = names [0]
names.sort()
namesScore = 0
for name in names:
    nameSum = 0
    for character in name:
        if character != '"':
            number = ord(character) - 64
            nameSum += number
    nameScore = nameSum * (names.index(name) +1)
    namesScore += nameScore
print("The total of all the name scores in the file ",namesScore)
