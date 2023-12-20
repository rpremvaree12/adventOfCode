with open("day1input.txt") as file:
    data = file.readlines()

# PART ONE

# numbers_part_one = []
# for line in data:
#     for c in line.strip():
#         # check if number
#         if c.isnumeric():
#             first_num = c
#             break

#     for c in line.strip()[::-1]:
#         if c.isnumeric():
#             second_num = c
#             break
    
#     numbers_part_one.append(int(first_num+second_num))

# print(sum(numbers_part_one))

# PART TWO
number_words = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
numbers_part_two = []



# finds word only if found in numerical order. "seven" is found but "eight" is earlier.
word_loc = len(data[2].strip())
for word in number_words:
    if data[2].find(word) >= 0:
        new_word_loc = data[2].find(word)
        
        if new_word_loc < word_loc:
            word_loc = new_word_loc
            found_word = word
        else:
            word_loc = -1
    print(word_loc, found_word)


#finds number    
# for c in line:
#     if c.isnumeric():
#         num_loc = line.find(c)
#         found_num = c
#         break

# if word_loc < num_loc and word_loc != -1:
#     first_num = number_words[found_word]
# else:
#     first_num = found_num

# numbers_part_two.append(first_num)

# print(numbers_part_two[0:5])
# output is ['4', '3', '7', '3', '1']
# finds word only if found in numerical order. "seven" is found but "eight" is earlier.