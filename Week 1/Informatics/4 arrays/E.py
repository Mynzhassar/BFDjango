n = int(input())
nums = [int(x) for x in input().split()]
same_sign = False

for i in range(len(nums) - 1):
	if (nums[i] > 0 and nums[i + 1] > 0) or (nums[i] < 0 and nums[i + 1] < 0):
		same_sign = True
		break

if same_sign: print("YES")
else: print("NO")
