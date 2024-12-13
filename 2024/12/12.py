input = open("input").read().strip()


def get_lines(plots, grid):
    corners = 0
    for pos in plots:
        outfacing = set()
        rns = set()
        for n in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (pos[0]+n[0], pos[1]+n[1]) not in plots:
                outfacing.add(n)

        corner_dir_pairs = [
            [(-1, 0), (0, -1)], [(-1, 0), (0, 1)],
            [(1, 0), (0, -1)], [(1, 0), (0, 1)]
        ]
        for corner_pair in corner_dir_pairs:
            if corner_pair[0] in outfacing and corner_pair[1] in outfacing:
                print("Outside")
                corners += 1

            corner_pair_abs = [(pos[0] + corner_pair[0][0], pos[1] + corner_pair[0][1]),
                               (pos[0] + corner_pair[1][0], pos[1] + corner_pair[1][1])]

            if corner_pair_abs[0] in plots and corner_pair_abs[1] in plots:
                if 0 <= corner_pair_abs[0][0] < len(grid[0]) and 0 <= corner_pair_abs[0][1] < len(grid) and 0 <= corner_pair_abs[1][0] < len(grid[0]) and 0 <= corner_pair_abs[1][1] < len(grid):
                    if (pos[0] + corner_pair[0][0] + corner_pair[1][0], pos[1] + corner_pair[0][1] + corner_pair[1][1]) not in plots:
                        print("Inside")
                        corners += 1

    print("plots", plots)
    print("corners", corners)
    return corners


def get_cost(pos,  grid):
    visited_plot = set()
    char = grid[pos[1]][pos[0]]

    def traverse(pos):
        if pos in visited_plot:
            return 0
        visited_plot.add(pos)
        visited.add(pos)
        perimiter = 0
        for n in [(pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0], pos[1]-1)]:
            if 0 <= n[0] < len(grid[0]) and 0 <= n[1] < len(grid):
                if grid[n[1]][n[0]] == char:
                    perimiter += traverse((n[0], n[1]))
                else:
                    perimiter += 1
            else:
                perimiter += 1
        return perimiter

    perimeter = traverse(pos)

    return (perimeter, len(visited_plot), get_lines(visited_plot, grid))


grid = [[c for c in line] for line in input.split("\n")]
visited = set()
sum1 = 0
sum2 = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if not (x, y) in visited:
            p, n, l = get_cost((x, y), grid)
            sum1 += p*n
            sum2 += l*n

print(sum1)
print(sum2)
