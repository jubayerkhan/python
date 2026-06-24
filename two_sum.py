
def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], index]
        seen[value] = index

print(two_sum([2,7,11,15], 13))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))