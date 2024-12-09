from collections import defaultdict
input = open("input").read().strip()

free2 = defaultdict(list)


def get_disk(input):
    index = 0
    disk = ""
    for i, c in enumerate(input):
        if i % 2 == 0:
            disk += (int(c))*(str(i//2) + " ")
            index += int(c)
        else:
            free2[index] = [0, int(c)]
            disk += (int(c))*("." + " ")
            index += int(c)
    return disk.strip().split(" ")


disk1 = get_disk(input)
disk2 = disk1.copy()
free_spaces = [i for i in range(len(disk1)) if disk1[i] == "."]

free_index = 0
for i in reversed(range(len(disk1))):
    if disk1[i] == ".":
        continue
    if free_spaces[free_index] > i:
        break
    disk1[free_spaces[free_index]] = disk1[i]
    disk1[i] = "."
    free_index += 1


sum1 = 0
for i, num in enumerate(disk1):
    if num == ".":
        break
    sum1 += i * int(num)
print(sum1)

curr_num = []
prev = ""
stop = 0
for i in reversed(range(len(disk2))):
    # stop += 1
    # if stop == 10:
    #     break
    if disk2[i] != prev and len(curr_num) > 0:
        # print(curr_num)
        for k, v in free2.items():
            # print(k, v)
            if k + v[0] > i:
                break
            if v[1] >= len(curr_num):
                ii = 0
                for num in curr_num:
                    disk2[v[0]+k+ii] = num
                    ii += 1
                free2[k][0] += ii
                free2[k][1] -= ii
                for j in range(len(curr_num)):
                    # print(disk2[i+j+1])
                    disk2[i+j+1] = "."
                break

        curr_num = []
    prev = disk2[i]
    if disk2[i] != ".":
        curr_num.append(disk2[i])

sum2 = 0
for i, num in enumerate(disk2):
    if num == ".":
        continue
    sum2 += i * int(num)
print(sum2)
# print(free2)
# print(disk2)
