class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp[i][j]表示t1[0..i]和t2[0..j]的最长子序列
        #递推公式： if t1[i] != t2[j] :
        #               d[i][j] = min(d[i-1][j],d[i][j-1])
        #          else:
        #                d[i][j] = d[i-1][j-1] + 1
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[len(text1)][len(text2)]