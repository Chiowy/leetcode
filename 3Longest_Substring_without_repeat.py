class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        n = len(s)
        left = right = max = 0
        while right < n:
            if s[right] not in temp: 
                temp.add(s[right])
                right = right + 1
            else:
                temp.remove(s[left])
                left = left + 1
            if len(temp) > max: max = len(temp)
        return max
            