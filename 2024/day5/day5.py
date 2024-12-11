from collections import defaultdict
with open('sampleData.txt') as file:
    sampleData = file.readlines()

def parseData(data):
    pageRules = defaultdict(list)
    pageOrder = []
    for line in data:
        if '|' in line:
            pages = [int(i) for i in line.strip().split('|')]
            pageRules[pages[0]].append(pages[1])

    for line in data:
        if ',' in line:
            pageOrder.append([int(i) for i in line.split(',')])

    return pageRules, pageOrder

def findMiddlePage(line):
    return(line[len(line)//2])
    
samplePageRules, samplePageOrder = parseData(sampleData)

for update in samplePageOrder:
    findMiddlePage(update) ## gets the middle number of the line
    print(update)
    