# Uses python3
def edit_distance(s, t):
    #write your code here
    len_s = len(s)
    len_t = len(t)
    d = [[i] for i in range(len_s + 1)]
    d[0] = [j for j in range(len_t + 1)]
    for j in range(1, len_t + 1):
        for i in range(1, len_s + 1):
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                d[i].append(min(insertion, deletion, match))
            else:
                d[i].append(min(insertion, deletion, mismatch))
    return d[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
