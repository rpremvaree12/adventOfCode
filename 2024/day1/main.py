from collections import defaultdict

with open('day1input.txt') as file:
    inputData = file.readlines()

with open('sampleData.txt') as file:
    sampleData = file.readlines()

def cleanData(data):
    leftList = []
    rightList = []
    # split data into 2 lists as ints
    for line in data:
        if line != "":
            l = line.strip().split()
            leftList.append(int(l[0]))
            rightList.append(int(l[-1]))
    return leftList, rightList

def differenceTwoLists(data):
    ans = 0
    leftList = []
    rightList = []
    # split data into 2 lists as ints
    leftList, rightList = cleanData(data)

    # sort lists from low to high
    leftList.sort()
    rightList.sort()
    # find difference and add to total
    # is it always right - left? if distance, then abs
    for n in range(len(leftList)):
        ans += abs(rightList[n] - leftList[n])
   
    return ans

### PART ONE
# find total difference between left column 
# right column when sorted from low to high

# sampleAns for Part One should be 11
# 3-1 + 3 -2 + 3 -3 + 4-3 + 9-4
# 2 + 1 + 0 + 1 + 2 + 5
# print(differenceTwoLists(sampleData))
# print(differenceTwoLists(inputData))

### PART TWO
# find frequency of number in left list appears in right list
# mult frequency by each number in left list
def buildFrequencyMap(data):
    numFrequencyMap = defaultdict(int)
    leftList, rightList = cleanData(data)
    for n in rightList:
        if n in leftList:
            numFrequencyMap[n] += 1
        # not necessary since default dict
        # else:
        #     concordance[n] = 0
    return numFrequencyMap
# count number of times left value appears in right list
# create a set?

def calculateSimilarity(data):
    similarityScore = 0
    leftList, rightList = cleanData(data)
    concordance = buildFrequencyMap(data)
    for n in leftList:
        similarityScore += concordance[n] * n
    return similarityScore

# print(buildFrequencyMap(sampleData))
# print(calculateSimilarity(sampleData))
print(buildFrequencyMap(inputData))
# print(calculateSimilarity(inputData))

# all repeat numbers in inputdata

### post-mortem:
# buildFrequencyMap wasn't working for the longest time and only finding 1 instance
# thought it was because I wasn't building the map properly so used defaultdict
# defaultdict sets not found keys to 0 by default which helps handling keyErrors
# I needed to iterate through rightList to find if num exists in leftList
# and update count accordingly
# learned code was right but I really needed to understand the problem in order to solve it