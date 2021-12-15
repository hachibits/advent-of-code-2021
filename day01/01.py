nums = [int(line.strip()) for line in open("input")]
print(sum(b > a for a, b in zip(nums, nums[1:])))
