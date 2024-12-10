input = open("input").read().strip()


visited1 = set()
visited2 = []


def traverse(pos, height, grid):
    visited1.add(pos)
    visited2.append(pos)
    next_poses = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]),
                  (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
    for next_pos in next_poses:
        if 0 <= next_pos[0] < len(grid[0]) and 0 <= next_pos[1] < len(grid):
            if int(grid[next_pos[1]][next_pos[0]]) == height+1:
                traverse((next_pos[0], next_pos[1]), height+1, grid)


grid = [[c for c in line] for line in input.split("\n")]
sum1 = 0
sum2 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "0":
            traverse((x, y), 0, grid)
            for x1, y1 in visited1:
                if grid[y1][x1] == "9":
                    sum1 += 1
            for x2, y2 in visited2:
                if grid[y2][x2] == "9":
                    sum2 += 1
            visited1 = set()
            visited2 = []

print(sum1)
print(sum2)
