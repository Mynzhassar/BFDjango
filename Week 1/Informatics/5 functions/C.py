def exclusive_or(x, y):
	if x == y: return 0
	return 1

x, y = input().split()
print(exclusive_or(x, y))