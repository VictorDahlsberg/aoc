input = open("input").read().strip()


def is_possible_2(ans, nums, agg):
    if agg > ans:
        return False
    if len(nums) == 1:
        return agg * nums[0] == ans or agg + nums[0] == ans or int(str(agg) + str(nums[0])) == ans

    return is_possible_2(ans, nums[1:], agg + nums[0]) or is_possible_2(ans, nums[1:], agg * nums[0]) or is_possible_2(ans, nums[1:], int(str(agg) + str(nums[0])))


def is_possible_1(ans, nums, agg):
    if agg > ans:
        return False
    if len(nums) == 1:
        return agg * nums[0] == ans or agg + nums[0] == ans

    return is_possible_1(ans, nums[1:], agg + nums[0]) or is_possible_1(ans, nums[1:], agg * nums[0])


sum1 = 0
sum2 = 0
for line in input.split("\n"):
    left, right = line.split(":")
    ans = int(left.strip())
    nums = right.strip().split(" ")
    nums = [int(num) for num in nums]

    if is_possible_1(ans, nums[1:], nums[0]):
        sum1 += ans
    if is_possible_2(ans, nums[1:], nums[0]):
        sum2 += ans

print(sum1)
print(sum2)
