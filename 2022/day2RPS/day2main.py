with open("inputday2.txt") as file:
    data  = file.read().splitlines()

# PART ONE
# A,X = 1, B,Y = 2, C,Z = 3
# A - ROCK = 1
# B - SCISSOR = 2
# C - PAPER = 3
# X - ROCK = 1
# Y - SCISSOR = 2
# Z - PAPER = 3

values = {"A":1,
          "B":2,
          "C":3,

          "X":1,
          "Y":2,
          "Z":3}
# win = 6, draw = 3, lose = 0
split_data = [n.split() for n in data]

cleaned_data = []

for n in split_data:
    cleaned_data.append([values[n[0]],values[n[1]]])



