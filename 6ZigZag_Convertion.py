class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        # 生成 numRows 行空字符串
        res = ['' for _ in range(numRows)]

        # flag = -1 表示从下往上，flag = 1 表示从上往下
        i, flag = 0, -1
        for c in s:
            res[i] = res[i] + c
            if i == 0 or i == numRows-1: flag = -flag # 判断是否到达转折点，如果到达则反转
            i = i + flag

        return ''.join(res)
print(Solution().convert('as', 1))