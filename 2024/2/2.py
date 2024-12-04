input = open("input").read().strip()


def is_safe(nums):
    inc = int(nums[1]) > int(nums[0])
    for i in range(len(nums)-1):
        diff = int(nums[i+1]) - int(nums[i])
        if (inc and diff > 3) or (inc and diff < 1):
            return False
        if (not inc and diff < -3) or (not inc and diff > -1):
            return False
    return True


def is_safe_rec(nums, depth):  # Deos not work
    if depth > 1:
        return False
    inc = int(nums[1]) > int(nums[0])
    for i in range(len(nums)-1):
        diff = int(nums[i+1]) - int(nums[i])
        if diff == 0:
            return is_safe(nums[:i] + nums[i + 1:], depth+1) or is_safe(nums[:i+1] + nums[i+2:], depth + 1)
        elif (inc and diff > 3) or (inc and diff < 1):
            return is_safe(nums[:i] + nums[i + 1:], depth+1) or is_safe(nums[:i+1] + nums[i+2:], depth + 1)
        elif (not inc and diff < -3) or (not inc and diff > -1):
            return is_safe(nums[:i] + nums[i + 1:], depth+1) or is_safe(nums[:i+1] + nums[i+2:], depth + 1)
    return True


sum1 = 0
for line in input.split("\n"):
    nums = line.split(" ")
    if is_safe(nums):
        sum1 += 1


sum2 = 0
for line in input.split("\n"):
    nums = line.split(" ")
    valid = False
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            valid = True
            break

    if valid:
        sum2 += 1

print(sum1)
print(sum2)
