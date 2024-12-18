import numpy as np
import re

"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
"""

"""
A*X     A*Y  
B*X     B*Y

[AX, BX] , [AY,BY]
[PX, PY]
"""

with open('sampleData.txt') as file:
    machine = ""
    rawSampleData = []
    for line in file.readlines():
        if line == "\n":
            rawSampleData.append(machine.split("\n"))
            machine = ""
        else:
            machine += line
    # add last line
    rawSampleData.append(machine)

a = np.array([[94, 22], [34, 67]])
b = np.array([8400, 5400])
x = np.linalg.solve(a, b)

print(rawSampleData)