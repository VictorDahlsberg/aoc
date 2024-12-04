input = open("input").read().strip()

grid = [[c for c in line] for line in input.split("\n")]


def get_prod_of_surrouding_numbers(x_in, y_in):
    numbers = []
    for y in range(max(y_in-1, 0), min(y_in+2, len(grid))):
        skip_next = False
        for x in range(max(x_in-1, 0), min(x_in+2, len(grid[y]))):
            if skip_next:
                if not grid[y][x].isnumeric():
                    skip_next = False
                continue
            curr_num = ""
            if grid[y][x].isnumeric():
                x1 = x
                while (grid[y][x1]).isnumeric():
                    curr_num = grid[y][x1] + curr_num
                    if x1 > 0:
                        x1 -= 1
                x1 = x + 1
                while (grid[y][x1]).isnumeric():
                    curr_num += grid[y][x1]
                    if x1 < len(grid[y]) - 1:
                        x1 += 1
                    else:
                        break
                numbers.append(int(curr_num))
                skip_next = True
    if (len(numbers) == 2):
        return numbers[0] * numbers[1]
    else:
        return 0


def get_sum_of_surrouding_numbers(x_in, y_in):
    sum = 0
    for y in range(max(y_in-1, 0), min(y_in+2, len(grid))):
        skip_next = False
        for x in range(max(x_in-1, 0), min(x_in+2, len(grid[y]))):
            if skip_next:
                if not grid[y][x].isnumeric():
                    skip_next = False
                continue
            curr_num = ""
            if grid[y][x].isnumeric():
                x1 = x
                while (grid[y][x1]).isnumeric():
                    curr_num = grid[y][x1] + curr_num
                    if x1 > 0:
                        x1 -= 1
                x1 = x + 1
                while (grid[y][x1]).isnumeric():
                    curr_num += grid[y][x1]
                    if x1 < len(grid[y]) - 1:
                        x1 += 1
                    else:
                        break
                sum += int(curr_num)
                skip_next = True

    return sum


sum1 = 0
sum2 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        char = grid[y][x]
        if not char.isnumeric() and not char == ".":
            sum1 += get_sum_of_surrouding_numbers(x, y)
        if char == "*":
            sum2 += get_prod_of_surrouding_numbers(x, y)

print(sum1)
print(sum2)
