sum = 0

with open("input.txt") as file:
    for line in file:
        print(line)
        for c in line:
            if c.isnumeric():
                print(c)
                sum += int(c)*10
                break
        for c in reversed(line):
            if c.isnumeric():
                sum += int(c)
                print(c)
                break

print(sum)
