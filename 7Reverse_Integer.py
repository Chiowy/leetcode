class Solution:
    def reverse(self, x: int) -> int:

        temp =  list()
        a = x
        flag = 0
        if a < 0:
            a = -a
            flag = 1
        while a >= 10:
            temp.append(a%10)
            a = int(a/10)
        temp.append(a)
        
        a = 0
        for i in temp:
            a = i + a*10

        if flag: a = -a
        if a <= -pow(2,31) or a >= pow(2,31)-1:
            return 0 

        return a

print(Solution().reverse(1534236469))