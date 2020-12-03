with open("inputday3.txt") as inputfile:
    lines = [line.split() for line in inputfile]

countLines = 0
for i in lines:
    countLines += 1

countRow = 0
for char in lines[0][0]:
    countRow += 1

def day3(shiftY, shiftX):
    x = 0
    y = 0
    counter = 0
    index = 0

    while x < countLines - 1:
        y += shiftY
        x += shiftX

        if y >= countRow - 1:
            y = y - countRow

        index = lines[x][0]
        cell = index[y]

        
        if cell == '#':
            counter += 1

    return counter

result = day3(1, 1) * day3(3, 1) * day3(5, 1) * day3(7, 1) * day3(1, 2)
print(result)