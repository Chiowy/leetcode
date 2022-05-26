"""Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward
"""
class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # palidrome integer must be positive
            return False
        else:
            str_x = str(x)
            head = 0 # 初始化head指针
            tail = len(str_x) - 1 # 初始化tail
            while head <= tail:
                if str_x[head] != str_x[tail]:
                    return False
                head += 1
                tail -= 1
        
        return True


print(Solution().isPalindrome(10))

"""RESULT
Runtime: 105 ms, faster than 28.92% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 16.34% of Python3 online submissions for Palindrome Number.
"""