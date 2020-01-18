if __name__ == '__main__':
    mark_sheet = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark_sheet.append([name, score])
        scores.append(score)

    
    second_highest = sorted(list(set(scores)))[1]
    for name, score in sorted(mark_sheet):
        if score == second_highest: print(name)


