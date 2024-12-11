with open('sampleData.txt') as file:
    rawSampleData = file.read()

with open('inputData.txt') as file:
    rawInputData = file.read()

def parseData(data):
    reportData = []
    for level in data.split('\n'):
        reportData.append([int(n) for n in level.split()])
    return reportData

def isSafePartOne(reportData):
    numSafe = 0
    for report in reportData:
        if isSafe(report):
            numSafe += 1
    return numSafe

def isSafe(report):
    # check if the report is in increasing or decreasing order by checking the original list against a sorted list
    inc = report == sorted(report)
    dec =  report == sorted(report,reverse=True)
    # check if differences no greater than 3 and less than 1
    if inc and differenceOfThreeIncreasing(report) or differenceOfThreeDecreasing(report) and dec:
        return True
    return False

# def isSafePartTwo(reportData):
    


def differenceOfThreeIncreasing(report):
    for i in range(len(report)-1):
        if (report[i+1] - report[i]) > 3 or (report[i+1] - report[i]) < 1:
            return False
    return True

def differenceOfThreeDecreasing(report):
    for i in range(len(report)-1):
        # print(f"{report[i+1]}-{report[i]}")
        if (report[i+1] - report[i]) < -3 or (report[i+1] - report[i]) > -1:
            return False
    return True

# Part Two
"""
7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
"""

# Part One
"""
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
"""


sampleData = parseData(rawSampleData)
print(isSafePartOne(sampleData))

# inputData = parseData(rawInputData)
# print(isSafe(inputData))
