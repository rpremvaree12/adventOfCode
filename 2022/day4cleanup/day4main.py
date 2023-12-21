with open("day4input.txt") as f:
    data = f.read().splitlines()

sample_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split()

def create_sections(data):
    sections = [d.split(",") for d in data]
    return sections

sample_sections = create_sections(sample_data)

def clean_str(string):
    return [int(s) for s in string if s.isnumeric()]
print(clean_str(sample_sections[0][0]))



sections = create_sections(data)

