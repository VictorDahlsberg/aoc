from functools import cache
input = open("input").read().strip()
rows = [line for line in input.split("\n")]
words = rows[0].split(", ")
problems = rows[2:]

sum = 0


@cache
def num_possible(problem):
    if not problem:
        return 1
    sum = 0
    for word in words:
        if problem.startswith(word):
            sum += num_possible(problem[len(word):])
    return sum


sum1 = 0
sum2 = 0
for problem in problems:
    combs = num_possible(problem)
    if combs:
        sum1 += 1
    sum2 += combs

print(sum1)
print(sum2)
