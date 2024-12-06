with open ('sampleData.txt') as file:
    sampleData = [line for line in file.readlines()]

def findGuard(data):
    for row, line in enumerate(data):
        if '^' in line:
            return f"found on row {row} at col {line.index('^')}"

print(findGuard(sampleData))

def displayGrid(data):
    return("".join(data))

print(displayGrid(sampleData))