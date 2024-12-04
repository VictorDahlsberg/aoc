input = open("input").read().strip()
grid = [[c for c in line] for line in input.split("\n")]
rows = len(grid)
cols = len(grid[0])


def is_xmas(depth, x, y, dx, dy):
    if x+dx < 0 or x + dx >= cols:
        return 0
    if y+dy < 0 or y + dy >= rows:
        return 0

    if depth == 0:
        if grid[y+dy][x+dx] == "M":
            return is_xmas(1, x+dx, y+dy, dx, dy)
    elif depth == 1:
        if grid[y+dy][x+dx] == "A":
            return is_xmas(2, x+dx, y+dy, dx, dy)
    elif depth == 2:
        if grid[y+dy][x+dx] == "S":
            return 1

    return 0


def is_cross_mas(x, y):
    if x-1 < 0 or x + 1 >= cols:
        return 0
    elif y-1 < 0 or y + 1 >= rows:
        return 0

    elif (((grid[y-1][x-1] == "M" and grid[y+1][x+1] == "S") or
            (grid[y-1][x-1] == "S" and grid[y+1][x+1] == "M")) and
            ((grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S") or
             (grid[y-1][x+1] == "S" and grid[y+1][x-1] == "M"))):
        return 1

    else:
        return 0


sum1 = 0
sum2 = 0
for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "X":
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    sum1 += is_xmas(0, x, y, dx, dy)

        elif grid[y][x] == "A":
            sum2 += is_cross_mas(x, y)


print(sum1)
print(sum2)
