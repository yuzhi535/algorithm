''' 编辑距离问题 动态规划 '''
def editDis(s1: str, s2: str):
    l1, l2 = len(s1), len(s2)
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, min(dp[i][j-1]+1, dp[i-1][j-1]+1))
    return dp[len(s1)][len(s2)]


s1 = "jary"
s2 = 'jerry'
print(editDis(s1, s2))
