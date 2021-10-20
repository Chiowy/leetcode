class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        elif x == 0: return True
        else:
            if x > 2**31 - 1 or x < -2**31:
                return False
            else:
                temp = list()
                while x >= 10:
                    temp.append(x%10) #2324%10=4
                    x = int(x / 10) # x = 2324 x = 232
                temp.append(x)

                head, tail = 0, len(temp) - 1
                while head < tail:
                    if temp[head] != temp[tail]: return False
                    head = head + 1
                    tail = tail - 1

        return True


print(Solution().isPalindrome(10))