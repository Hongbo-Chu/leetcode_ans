def minDistance(word1: str, word2: str) -> int:
    ##用dp解题
    # 建立数组
    res = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]  # 字符从1开始0用来初始化
    # res = [[0]*3]*3为什么这样定义不可以 这样定义改d[1][2]会改d[x][2]
    for i in range(len(word2)+1):
        res[0][i] = i
    for j in range(len(word1)+1):
        res[j][0] = j

    for i in range(1, len(word1)+1 ):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                res[i][j] = min(res[i - 1][j], res[i][j - 1], (res[i - 1][j - 1]-1)) + 1
            else:
                res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1]) + 1
    return res[len(word1)][len(word2)]



print(minDistance("intention","execution"))
