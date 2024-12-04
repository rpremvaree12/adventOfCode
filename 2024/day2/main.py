with open('sampleData.txt') as file:
    rawSampleData = file.read()

with open('inputData.txt') as file:
    rawInputData = file.read()


def parseData(data):
    reportData = []
    for level in data.split('\n'):
        reportData.append([int(n) for n in level.split()])
    return reportData

def checkReport(reportData):
    numSafe = 0
    for report in reportData:
        isSafe = True
        if report[0] > report[1]:
            # levels should be decreasing
            print("Levels Decreasing!")
            isSafe = checkDecreasingLevels(report)
        else:
            # levels should be increasing
            print("Levels Increasing!")
            isSafe = checkIncreasingLevels(report)
        print(report)
        if isSafe: numSafe += 1
        if isSafe:
            print("Safe")
        else:
            print("Unsafe")
        # if isSafe: numSafe += 1
    return numSafe


def checkDecreasingLevels(report):
    numError = 0
    for i in range(len(report)-1):
        if report[i] <= report[i+1] or (report[i+1] - report[i]) < -3:
            numError += 1
            if numError >2:
                return False
    return True

def checkIncreasingLevels(report):
    numError = 0
    for i in range(len(report)-1):
        if report[i] >= report[i+1] or (report[i+1] - report[i]) > 3:
            numError += 1
            if numError >2:
                return False
    return True

sampleData = parseData(rawSampleData)
print(checkReport(sampleData))
"""
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
"""
# inputData = parseData(rawInputData)
# print(checkReport(inputData))