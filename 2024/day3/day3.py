import re

with open('inputData.txt') as file:
    inputData = "do()" + file.read()
    inputData = inputData.split()

sampleText1 = "do()" + "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

cleanSampleText1 = re.findall("mul\(\d{1,3},\d{1,3}\)",sampleText1)

sampleText2 ="do()"+"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
cleanSampleText2 = sampleText2.split('do()')


def sumMuls(line):
    sum = 0
    cleanLine = re.findall("mul\(\d{1,3},\d{1,3}\)",line)
    # print(cleanLine)
    for t in cleanLine:
        t = t[4:-1]
        nums = [int(num) for num in t.split(',')]
        sum += nums[0] * nums[1]
    return sum

def findDont(line):
    sum = 0
    match = "don't()"
    cleanLine = line.split("do()")
    for l in cleanLine:
        l = re.sub(f"{match}.*", "", l)
        sum += sumMuls(l)
    return sum

def partTwo(data):
    totalSum = 0
    for l in data:
        totalSum += findDont(l)
    return totalSum

# The pattern \(.*?\):
# \(: Matches an opening parenthesis.
# .*?: Matches any number of characters (non-greedy).
# \): Matches a closing parenthesis.
# print(sumMuls(cleanSampleText))

def partOne(data):
    totalSum = 0
    for l in data:
        totalSum+=sumMuls(l)
        
    return totalSum

# print(partOne(inputData))
print(partTwo(inputData))