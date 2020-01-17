def power(a, n):
	a, n = float(a), int(n)
	if n == 0: return 1
	
	cur = a
	for _ in range(n - 1): a *= cur
	return a

a, n = input().split()
print(power(a, n))