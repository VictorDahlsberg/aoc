from collections import defaultdict
input = open("input").read().strip()


def get_visited(pos, grid):
    visited = set()
    visited_dirrs = defaultdict(set)
    dirr = 0

    while True:
        visited.add(pos)
        if dirr in visited_dirrs[pos]:
            return visited, True
        visited_dirrs[pos].add(dirr)
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


def get_walls(visited):
    walls = set()
    for x, y in visited[0]:
        if grid[y][x] == ".":
            grid[y][x] = "#"
            if get_visited((42, 83), grid)[1]:
                walls.add((x, y))
            grid[y][x] = "."
    return walls


def get_walls_2():
    walls = set()
    for y in range(130):
        for x in range(130):
            if grid[y][x] == ".":
                grid[y][x] = "#"
                if get_visited((42, 83), grid)[1]:
                    walls.add((x, y))
                grid[y][x] = "."
    return walls


grid = [[c for c in line] for line in input.split("\n")]

visited = get_visited((42, 83), grid)
print(len(visited[0]))
print(len(get_walls(visited)))
print(len(get_walls_2()))
