base = []


def LS(i: int, j: int, s):
    if i < 0 or j < 0:
        return
    if base[i][j] == 1:
        LS(i-1, j-1, s)
        print(s[i-1], end=' ')
    elif base[i][j] == 2:
        LS(i, j-1, s)
    elif base[i][j] == 3:
        LS(i-1, j, s)


def LCS(s1: str, s2: str):
    sz1 = len(s1)
    sz2 = len(s2)
    dp = [[0 for j in range(sz2+1)] for i in range(sz1+1)]
    global base
    base = [[0 for j in range(sz2+1)] for i in range(sz1+1)]

    for i in range(1, sz1+1):
        for j in range(1, sz2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                base[i][j] = 1
            elif dp[i][j-1] >= dp[i-1][j]:
                dp[i][j] = dp[i][j-1]
                base[i][j] = 2
            else:
                dp[i][j] = dp[i-1][j]
                base[i][j] = 3
    LS(sz1, sz2, s1)
    print("\n", end='')
    return dp[sz1][sz2]


s2 = '12354'
s1 = 'as12b35452234'
print(LCS(s1, s2))
