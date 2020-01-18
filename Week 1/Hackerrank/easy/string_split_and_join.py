def split_and_join(line):
    words = []
    cur = ""
    for i in range(len(line)):
        if line[i] != " ": cur += line[i]
        if line[i] == " " or i == len(line) - 1: 
            words.append(cur)
            cur = ""

    res = ""
    for ind, word in enumerate(words):
        res += word
        if ind != len(words) - 1: res += "-"

    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)