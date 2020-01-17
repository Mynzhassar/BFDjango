n = int(input())
nums = [int(x) for x in input().split()]
cnt = 0
for num in nums: cnt += num > 0

print(cnt)
