n = int(input())
nums = [int(x) for x in input().split()]
for num in nums:
	if num % 2 == 0: print(num, end = " ")
