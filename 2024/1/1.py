input = open("input").read().strip()
left_list = []
right_list = []

for line in input.split("\n"):
    left, right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

sum1 = 0

for i in range(len(left_list)):
    sum1 += abs(left_list[i] - right_list[i])

print(sum1)

sum2 = 0

for num in left_list:
    sum2 += right_list.count(num) * num

print(sum2)
