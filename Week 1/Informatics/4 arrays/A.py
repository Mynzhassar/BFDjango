n = int(input())
nums = [int(x) for x in input().split()]
for i, num in enumerate(nums):
	if i % 2 == 0: print(num, end = " ")