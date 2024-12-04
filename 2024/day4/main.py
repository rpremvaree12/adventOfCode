import re

def parseData(data):
    with open(data) as file:
        return file.read()

sampleData = parseData("sampleData.txt") # data as a string

# check for XMAS using regex findall
# forward -done
# backward -done
# down -done
# up -done
# diagonally down-right
# diagonally down-left
# diagonally up-right
# diagonally up-left

rowsData = sampleData.split()
colsData = ""

# go through every row and add the letter in the same column

for rowNum in range(len(rowsData)):
    for line in rowsData:
        colsData += line[rowNum]

fwCount = re.findall("XMAS",sampleData)
print(f'forward count: {len(fwCount)}')

bwCount = re.findall("XMAS",sampleData[::-1])
print(f'backward count: {len(bwCount)}')

downCount = re.findall("XMAS",colsData)
print(f'down count: {len(downCount)}')

upCount = re.findall("XMAS",colsData[::-1])
print(f'up count: {len(upCount)}')

diagonalData = []
for rowNum in range(6):
    for colNum in range(6):
        diagonal = ""
        for line in rowsData:
            diagonal += rowsData[colNum]
            diagonal += rowsData[colNum+1]
            diagonal += rowsData[colNum+2]
            diagonal += rowsData[colNum+3]
            diagonalData.append(diagonal)

print(diagonalData)

diagonalDownCount = re.findall("XMAS",diagonalData)
print(len(diagonalDownCount))

diagonalData = []
# for colNum in range(6):
#     diagonal = ""
#     for line in rowsData:
#         diagonal += rowsData[colNum]
#         diagonal += rowsData[colNum+1]
#         diagonal += rowsData[colNum+2]
#         diagonal += rowsData[colNum+3]
#         diagonalData.append(diagonal)
#         print(diagonalData)