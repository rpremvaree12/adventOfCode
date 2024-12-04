import re

def parseData(data):
    with open(data) as file:
        return file.read()

sampleData = parseData("sampleData.txt")

fwCount = re.findall("XMAS",sampleData)
print(f'forward count: {len(fwCount)}')

bwCount = re.findall("XMAS",sampleData[::-1])
print(f'backward count: {len(bwCount)}')

downCount = 0
rowsData = sampleData.split()
colsData = ""
for col in range(len(rowsData)):
    for line in rowsData:
        colsData += line[col]
downCount = re.findall("XMAS",colsData)
print(f'down count: {len(downCount)}')

upCount = re.findall("XMAS",colsData[::-1])
print(f'up count: {len(upCount)}')
