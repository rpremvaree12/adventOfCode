from collections import defaultdict

with open('day1input.txt') as afile:
    inputData = afile.readlines()

with open('sampleData.txt') as bfile:
    sampleData = bfile.readlines()

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
def buildConcordance(data):
    concordance = defaultdict(int)
    leftList, rightList = cleanData(data)
    for n in rightList:
        if n in leftList:
            concordance[n] += 1
        else:
            concordance[n] = 0
    return concordance
# count number of times left value appears in right list
# create a set?

def calculateSimilarity(data):
    similarityScore = 0
    leftList, rightList = cleanData(data)
    concordance = buildConcordance(data)
    for n in leftList:
        similarityScore += concordance[n] * n
    return similarityScore

# print(buildConcordance(sampleData))
# print(calculateSimilarity(sampleData))
# print(buildConcordance(inputData))
print(calculateSimilarity(inputData))

# all repeat numbers in inputdata
"""
92869
64678
60853
25580
14549
26820
92950
59882
41310
82400
85661
74691
23116
75812
47324
14510
41051
39776
33984
84872
82391
65185
48400
77539
83731
44753
18829
36777
74877
83870
35610
66508
42459
99057
81159
47115
70501
34199
20602
82455
82947
16859
76135
78088
10638
"""