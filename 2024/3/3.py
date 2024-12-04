import re
input = open("input").read().strip()
matches = re.findall(r'mul\(\d+,\d+\)', input)
matches2 = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', input)

sum1 = 0
for match in matches:
    l, r = match[4:-1].split(",")
    sum1 += int(l)*int(r)


sum2 = 0
enabled = True
for match in matches2:
    if match == "don't()":
        enabled = False

    elif match == "do()":
        enabled = True

    elif enabled:
        l, r = match[4:-1].split(",")
        sum2 += int(l)*int(r)


print(sum1)
print(sum2)
