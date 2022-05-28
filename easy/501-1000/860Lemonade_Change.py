"""
找钱: 每个5$, 一开始没钱, 只能用前面赚的钱找零, 只有5, 10 ,20面值的货币
先建立一个字典, lile {5:1, 10:2, 20:1}
对每一个顾客。应找 i - 5 $
优先使用大面值的找零
"""
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        myband = {5:0, 10:0, 20:0}  # 建立字典
        for i in bills:  # 对每一个客户
            myband[i] += 1  # 先收钱
            change = i - 5
            # 如果刚好为 5 元, 则change=0, 不用找零
            if change == 5:  # 如果change=5
                if myband[5] == 0:  # 是否有5$的零钱
                    return False  # 没有
                else:  # 有
                    myband[5] -= 1  # 用掉一个5$
            if change == 15:  # 如果change=15
                if myband[10] == 0:  # 是否有10$的零钱
                    if myband[5] >= 3:  # 没有的话，是否至少有三张5$
                        myband[5] -= 3  # 给出
                    else:
                        return False
                else:  # 有的话
                    if myband[5] >= 1:  # 是否至少有一张5$
                        myband[10] -= 1
                        myband[5] -= 1
                    else:
                        return False
        return True

solution = Solution()
print(solution.lemonadeChange(bills = [5,5,10,10,20]))

        