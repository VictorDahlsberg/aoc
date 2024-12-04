input = open("input").read().strip()
cubes = {"red": 12, "green": 13, "blue": 14}
sum1 = 0

for id, line in enumerate(input.split("\n")):
    games = line.split(":")[1].strip().split(";")
    valid = True
    for game in games:
        for value_color in game.split(","):
            value, color = value_color.strip().split(" ")
            if int(value) > cubes[color]:
                valid = False
                break
    if (valid):
        sum1 += id + 1

print(sum1)

sum2 = 0

for id, line in enumerate(input.split("\n")):
    games = line.split(":")[1].strip().split(";")
    min = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        for value_color in game.split(","):
            value, color = value_color.strip().split(" ")
            if int(value) > min[color]:
                min[color] = int(value)

    sum2 += min["red"] * min["green"] * min["blue"]

print(sum2)
