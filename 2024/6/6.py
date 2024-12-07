input = open("input").read().strip()


def get_visited(pos, grid):
    visited = set()
    visited_dirrs = set()
    dirr = 0

    while True:
        visited.add(pos)
        # if pos[0] == 41:
        # print(pos)
        if (pos[0], pos[1], dirr) in visited_dirrs:
            return visited, True
        visited_dirrs.add((pos[0], pos[1], dirr))
        directions = [(pos[0], pos[1] - 1), (pos[0] + 1, pos[1]),
                      (pos[0], pos[1] + 1), (pos[0] - 1, pos[1])]

        while True:
            nextPos = directions[dirr]
            if not (len(grid[0]) > nextPos[0] >= 0 and len(grid) > nextPos[1] >= 0):
                return visited, False
            elif grid[nextPos[1]][nextPos[0]] == ".":
                break
            dirr = (dirr + 1) % 4
            nextPos = directions[dirr]

        pos = nextPos


def get_walls(visited, start_pos):
    walls = set()
    for x, y in visited[0]:
        if grid[y][x] == ".":
            grid[y][x] = "#"
            if get_visited(start_pos, grid)[1]:
                walls.add((x, y))
            grid[y][x] = "."
    return walls


def get_start_pos(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                return (x, y)


grid = [[c for c in line] for line in input.split("\n")]
start_pos = get_start_pos(grid)
grid[start_pos[1]][start_pos[0]] = "."
visited = get_visited(start_pos, grid)
print(len(visited[0]))
print(len(get_walls(visited, start_pos)))
