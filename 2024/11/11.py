from functools import lru_cache


@lru_cache(maxsize=None)
def get_number_of_stones(stone, i, max):
    if i == max:
        return 1
    if stone == 0:
        return get_number_of_stones(1, i + 1, max)
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        return get_number_of_stones(int(str_stone[0: len(str_stone)//2]), i+1, max) + get_number_of_stones(int(str_stone[len(str_stone)//2:]), i+1, max)
    else:
        return get_number_of_stones(stone * 2024, i+1, max)


stones = [int(stone) for stone in open("input").read().strip().split()]
sum1 = 0
sum2 = 0


for stone in stones:
    sum1 += get_number_of_stones(stone, 0, 25)
    sum2 += get_number_of_stones(stone, 0, 75)

print(sum1)
print(sum2)
