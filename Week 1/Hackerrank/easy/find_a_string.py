def count_substring(string, sub_string):
    sub_strings = []
    for i in range(len(string) - len(sub_string) + 1):
        cur = ""
        for j in range(len(sub_string)): cur += string[i + j]
        sub_strings.append(cur)

    cnt = 0

    for sub in sub_strings:
        if sub == sub_string: cnt += 1
    return cnt

if __name__ == '__main__':