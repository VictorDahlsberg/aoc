sum = 0

numbers = {"one": "o1e",
           "two": "t2o",
           "three": "t3e",
           "four": "f4r",
           "five": "f5e",
           "six": "s6x",
           "seven": "s7n",
           "eight": "e8t",
           "nine": "n9e"}


def replace_words(text):
    for k, v in numbers.items():
        text = text.replace(k, v)
    return text


input = replace_words(open("input.txt").read())

lines = input.split("\n")

for line in lines:
    print(line)
    for c in line:
        if c.isnumeric():
            sum += int(c) * 10
            break
    for c in reversed(line):
        if c.isnumeric():
            sum += int(c)
            break

print(sum)
