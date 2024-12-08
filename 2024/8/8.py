from collections import defaultdict
input = open("input").read().strip()


def get_nodes_2(antennas, width, height):
    nodes = set()
    for ants in antennas.values():
        for index, a1 in enumerate(ants):
            if index < len(ants)-1:
                for a2 in ants[index+1:]:
                    diff = (a2[0]-a1[0], a2[1] - a1[1])
                    pos = a1
                    while 0 <= pos[0] < width and 0 <= pos[1] < height:
                        nodes.add(pos)
                        pos = (pos[0] + diff[0], pos[1] + diff[1])
                    pos = a1
                    while 0 <= pos[0] < width and 0 <= pos[1] < height:
                        nodes.add(pos)
                        pos = (pos[0] - diff[0], pos[1] - diff[1])

    return nodes


def get_nodes(antennas, width, height):
    nodes = set()
    for ants in antennas.values():
        for index, a1 in enumerate(ants):
            if index < len(ants)-1:
                for a2 in ants[index+1:]:
                    diff = (a2[0]-a1[0], a2[1] - a1[1])
                    n1 = (a1[0] + 2 * diff[0], a1[1] + 2*diff[1])
                    n2 = (a2[0] - 2 * diff[0], a2[1] - 2*diff[1])
                    if 0 <= n1[0] < width and 0 <= n1[1] < height:
                        nodes.add(n1)
                    if 0 <= n2[0] < width and 0 <= n2[1] < height:
                        nodes.add(n2)
    return nodes


def get_antennas(grid):
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != ".":
                antennas[grid[y][x]].append((x, y))
    return antennas


grid = [[c for c in line] for line in input.split("\n")]
ants = get_antennas(grid)
nodes = get_nodes(ants, len(grid), len(grid[0]))
print(len(nodes))
nodes_2 = get_nodes_2(ants, len(grid), len(grid[0]))
print(len(nodes_2))
