import re

sampleText = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

cleanText = re.findall("/mul\(.*?\)/g",sampleText)
# The pattern \(.*?\):
# \(: Matches an opening parenthesis.
# .*?: Matches any number of characters (non-greedy).
# \): Matches a closing parenthesis.

for t in cleanText:
    print(t.split("mul("))