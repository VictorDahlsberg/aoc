input = open("input").read().strip()

grid = [[c for c in line] for line in input.split("\n")]
print(grid)

posX = 42
posY = 83
visited = set()
dirr = 0

while True:
    u = (posX, posY-1)
    r = (posX+1, posY)
    d = (posX, posY+1)
    l = (posX-1, posY)
    print(posX, posY)
    print(dirr)
    if dirr == 0:
        if u[1] < 0:
            break;
        if grid[u[1]][u[0]] == ".":
            posX = u[0]
            posY = u[1]
        elif grid[u[1]][u[0]] == "#" and grid[r[1]][r[0]] != "#":
            dirr = (dirr + 1) % 4
            posX = r[0]
            posY = r[1]
        else:
            dirr = (dirr + 2) % 4
            posX = d[0]
            posY = d[1]
        visited.add((posX, posY))

    elif dirr == 1:
        if r[0] >= len(grid[0])-1:
            break;
        if grid[r[1]][r[0]] == ".":
            posX = r[0]
            posY = r[1]
        elif grid[r[1]][r[0]] == "#" and grid[d[1]][d[0]] != "#":
            dirr = (dirr + 1) % 4
            posX = d[0]
            posY = d[1]
        else:
            dirr = dirr + 2 % 4
            posX = l[0]
            posY = l[1]
        visited.add((posX, posY))

    elif dirr == 2:
        if d[1] >= len(grid)-1:
            break;
        if grid[d[1]][d[0]] == ".":
            posX = d[0]
            posY = d[1]
        elif grid[d[1]][d[0]] == "#" and grid[l[1]][l[0]] != "#":
            dirr = (dirr + 1) % 4
            posX = l[0]
            posY = l[1]
        else:
            dirr = (dirr + 2) % 4
            posX = u[0]
            posY = u[1]
        visited.add((posX, posY))
    elif dirr == 3:
        if l[0] < 0:
            break;
        if grid[l[1]][l[0]] == ".":
            posX = l[0]
            posY = l[1]
        elif grid[l[1]][l[0]] == "#" and grid[u[1]][u[0]] != "#":
            dirr = (dirr + 1) % 4
            posX = u[0]
            posY = u[1]
        else:
            dirr = (dirr + 2) % 4
            posX = r[0]
            posY = r[1]
        visited.add((posX, posY))

print(len(visited))
