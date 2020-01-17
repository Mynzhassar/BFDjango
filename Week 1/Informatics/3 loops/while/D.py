n = int(input())
is_power = True

while n != 1:
	if n % 2 == 0:
		n /= 2
	else:
		is_power = False
		print("NO")
		break

if is_power: print("YES")