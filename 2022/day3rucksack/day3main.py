with open("day3input.txt") as f:
    data = f.read().splitlines()

# PART ONE
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment, while 
# the second half of the characters represent items in the second compartment.

def find_item(string):
    half_index = int(len(string)/2)
    first_half = string[0:half_index]
    second_half = string[half_index:]

    for c in first_half:
        if second_half.find(c) != -1:
            loc = second_half.find(c)
            return second_half[loc]
    return "Not found"

def find_priority(char):
    if char.islower():
        return (ord(char)%97+1)
    else:
        return (ord(char)%65+27)

def sum_priorities():
    items = []
    for line in data:
        item = find_item(line)
        items.append(find_priority(item))
    return sum(items)


# PART TWO
# groups of 3 has badge. find the badge in each group.

def create_groups():
    groups = []
    group = []
    count = 0
    for line in data:
        group.append(line)
        count += 1
        if count > 2:
            groups.append(group)
            group = []
            count = 0
    return groups

elf_groups = create_groups()
sample_group = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg""".split()

def find_badge(group):
    for c in group[0]:
        if c in group[1] and c in group[2]:
            return find_priority(c)

print(find_badge(sample_group))

badges = []
for elf in elf_groups:
    for c in elf[0]:
        if c in elf[1] and c in elf[2]:
            badges.append(find_priority(c))