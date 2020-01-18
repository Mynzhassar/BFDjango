if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    values = list(dict.fromkeys(arr))
    values.sort()
    print(values[len(values) - 2])
