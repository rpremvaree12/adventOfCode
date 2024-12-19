import re

def parseData(data):
    with open(data) as file:
        return file.read()

# check for XMAS using regex findall
# forward -done 3
# backward -done 2
# down -done 1
# up -done 2
# diagonally down-right 1
# diagonally down-left 1
# diagonally up-right 4
# diagonally up-left 4

def findLRUD(dataString):
    rowsData = dataString.split()
    colsData = ""

    # go through every row and add the letter in the same column

    for rowNum in range(len(rowsData)):
        for line in rowsData:
            colsData += line[rowNum]

    fwCount = re.findall("XMAS",dataString)
    # print(f'forward count: {len(fwCount)}')

    bwCount = re.findall("XMAS",dataString[::-1])
    # print(f'backward count: {len(bwCount)}')

    downCount = re.findall("XMAS",colsData)
    # print(f'down count: {len(downCount)}')

    upCount = re.findall("XMAS",colsData[::-1])
    # print(f'up count: {len(upCount)}')
    return len(fwCount) + len(bwCount) + len(downCount) + len(upCount)


### worked on this with Margaret
def findDiagonals(dataList):
    height = len(dataList)
    width = len(dataList[0])

    downRightCount = 0
    downLeftCount = 0
    upRightCount = 0
    upLeftCount = 0
    for i in range(height):
        for j in range(width):
            if dataList[i][j] == 'X':
                if i < height - 3 and j < width - 3 and dataList[i + 1][j + 1] == 'M' and dataList[i + 2][j + 2] == 'A' and dataList[i + 3][j + 3] == 'S':
                    downRightCount += 1
                if i < height - 3 and j >= 3 and dataList[i + 1][j - 1] == 'M' and dataList[i + 2][j - 2] == 'A' and dataList[i + 3][j - 3] == 'S':
                    downLeftCount += 1
                if i >= 3 and j < width - 3 and dataList[i - 1][j + 1] == 'M' and dataList[i - 2][j + 2] == 'A' and dataList[i - 3][j + 3] == 'S':
                    upRightCount += 1
                if i >= 3 and j >= 3 and dataList[i - 1][j - 1] == 'M' and dataList[i - 2][j - 2] == 'A' and dataList[i - 3][j - 3] == 'S':
                    upLeftCount += 1
    return downRightCount + downLeftCount + upLeftCount + upRightCount

sampleDataString = parseData("sampleData.txt") # data as a string
sampleDataList = sampleDataString.split()

# print(findLRUD(sampleDataString) + findDiagonals(sampleDataList))

inputDataString = parseData("inputData.txt")
inputDataList = inputDataString.split()

print(findLRUD(inputDataString) + findDiagonals(inputDataList))

### TODO: to work on later
# diagonalData = []
# for rowNum in range(6):
#     for colNum in range(6):
#         diagonal = ""
#         for line in rowsData:
#             diagonal += rowsData[colNum]
#             diagonal += rowsData[colNum+1]
#             diagonal += rowsData[colNum+2]
#             diagonal += rowsData[colNum+3]
#             diagonalData.append(diagonal)

# print(diagonalData)

# diagonalDownCount = re.findall("XMAS",diagonalData)
# print(len(diagonalDownCount))

# diagonalData = []
# for colNum in range(6):
#     diagonal = ""
#     for line in rowsData:
#         diagonal += rowsData[colNum]
#         diagonal += rowsData[colNum+1]
#         diagonal += rowsData[colNum+2]
#         diagonal += rowsData[colNum+3]
#         diagonalData.append(diagonal)
#         print(diagonalData)