def average(array):
    distinct_heights = list(dict.fromkeys(array))
    return sum(distinct_heights)/len(distinct_heights)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)