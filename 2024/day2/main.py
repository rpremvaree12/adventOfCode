with open('sampleData.txt') as file:
    rawSampleData = file.read()

with open('inputData.txt') as file:
    rawInputData = file.read()

def parseData(data):
    reportData = []
    for level in data.split('\n'):
        reportData.append([int(n) for n in level.split()])
    return reportData

def isSafe(reportData):
    numSafe = 0
    for report in reportData:
        inc_or_dec = (report == sorted(report))or (report == sorted(report,reverse=True))
        # if inc_or_dec and differenceOfThree(report):
        #     numSafe += 1
    return numSafe

def differenceOfThree(report):
    for i in range(len(report)-1):
        if abs(report[i] - report[i+1]) < 3 and report[i] - report[i+1] > 1:
            print(report)
            return True
    return False
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
# inputData = parseData(rawInputData)
# print(isSafe(inputData))

sampleData = parseData(rawSampleData)
print(isSafe(sampleData))
