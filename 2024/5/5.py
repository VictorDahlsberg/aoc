from functools import cmp_to_key
input = open("input").read().strip()

pairs = [[x for x in line.split("|")] for line in input.split("\n")[:1176]]
lefts = [x[0] for x in pairs]
rights = [x[1] for x in pairs]
lines = [line.split(",") for line in input.split("\n")[1177:]]

invalid_lines = []
sum1 = 0
for line in lines:
    valid = True
    for i, num in enumerate(line):
        indices = [i for i, x in enumerate(rights) if x == num]
        for index in indices:
            if lefts[index] in line[i+1:]:
                valid = False
                break
    if valid:
        sum1 += int(line[len(line)//2])
    else:
        invalid_lines.append(line)


def compare(item1, item2):
    for i in range(len(lefts)):
        if lefts[i] == item1 and rights[i] == item2:
            return 1
        elif lefts[i] == item2 and rights[i] == item1:
            return -1

    return 0


sum2 = 0
for line in invalid_lines:
    sorted_line = sorted(line, key=cmp_to_key(compare))
    sum2 += int(sorted_line[len(line)//2])

print(sum1)
print(sum2)
