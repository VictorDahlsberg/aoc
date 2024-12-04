def get_points(winners, numbers):
    num_correct = 0
    for win in winners:
        num_correct += numbers.count(win)
    if num_correct > 0:
        return 2 ** (num_correct - 1)
    else:
        return 0


input = open("input").read().strip().replace("  ", " ")
sum1 = 0

for line in input.split("\n"):
    left, right = line.split(":")[1].strip().split("|")
    winners = left.strip().split(" ")
    numbers = right.strip().split(" ")
    sum1 += get_points(winners, numbers)

print(sum1)


def get_scratches(winners, numbers):
    num_correct = 0
    for win in winners:
        num_correct += numbers.count(win)
    return num_correct


scratches = [[[row.strip().split(" ") for row in line.split(":")[1].strip().split("|")]
              ]for line in input.split("\n")]


sum2 = 0
for i, scratch_series in enumerate(scratches):
    for scratch in scratch_series:
        sum2 += 1
        for j in range(get_scratches(scratch[0], scratch[1])):
            if i+j+1 < len(scratches):
                scratches[i+j+1].append(scratches[i+j+1][0])

print(sum2)
