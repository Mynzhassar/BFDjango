n = int(input())
nums = [int(x) for x in input().split()]
cnt = 0

for i in range(1, len(nums)): cnt += nums[i] > nums[i - 1]
print(cnt)
