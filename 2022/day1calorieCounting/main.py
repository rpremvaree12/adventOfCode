with open("inputday1.txt") as file:
    data  = file.read().strip()


# PART ONE
# Find the Elf carrying the most Calories.
# How many total Calories is that Elf carrying?

def elfCalories():
    elves = {}
    sum = 0
    num = 0
    for n in data:
        if n == "\n":
            elves[num] = sum
            sum = 0
            num += 1
        else:
            sum += int(n)
    return elves

topCal = max(elfCalories().values())
print(f"Largest calorie count is: {topCal}")


# PART TWO
# Elves would instead like to know the total Calories 
# carried by the top three Elves carrying the most Calories.
top1 = topCal
top2 = 0
top3 = 0
for n in elfCalories().values():
    if n > top2 and n < top1:
        top3 = top2
        top2 = n
    elif n > top3 and n < top2:
        top3 = n
    else:
        continue
print(f"{top1},{top2},{top3} = {top1 + top2 + top3}")