def minimum(nums):
	res = float("inf")
	for n in nums: 
		if n < res: res = n

	return res


nums = [int(x) for x in input().split()]
print(minimum(nums))