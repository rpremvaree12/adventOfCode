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
        for i in range(len(report)-1):
            print(report)
            if report[i] > report[i+1]:
                # levels should be decreasing
                print("Levels Decreasing!")
                isSafe = checkDecreasingLevels()
            else:
                # levels should be increasing
                print("Levels Increasing!")
                isSafe = checkIncreasingLevels()
            break
        # if isSafe: numSafe += 1
    return numSafe

def checkDecreasingLevels():
    pass

def checkIncreasingLevels():
    pass

sampleData = parseData(rawSampleData)
print(checkReport(sampleData))