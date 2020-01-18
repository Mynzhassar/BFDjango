if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = []
    pos = 0

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    ans.append([])
                    ans[pos] = [i, j, k]
                    pos += 1

    print(ans)

