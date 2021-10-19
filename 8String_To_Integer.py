import re

class Solution:
    def myAtoi(self, s: str) -> int:
        return int(*re.findall('^[\+\-]?\d+', s.lstrip()))

print(Solution().myAtoi('2321dfw131'))