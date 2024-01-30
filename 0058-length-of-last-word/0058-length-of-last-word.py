class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.strip().split(' ')
        l=len(str(words[-1]))
        return l