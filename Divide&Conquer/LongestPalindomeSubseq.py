class Solution:
    def __init__(self):
        self.memo = {}

    def longestPalindromeSubseq(self, s: str, idx1=0, idx2=None) -> int:
        if idx2 is None:
            idx2 = len(s) - 1

        if (idx1, idx2) in self.memo:
            return self.memo[(idx1, idx2)]
        if idx1 > idx2:
            return 0
        if idx1 == idx2:
            return 1
        if s[idx1] == s[idx2]:
            return 2 +  self.longestPalindromeSubseq(s, idx1+1, idx2-1)
        else:
            option1 = self.longestPalindromeSubseq(s, idx1, idx2-1)
            option2 = self.longestPalindromeSubseq(s, idx1+1, idx2)
            result = max(option1, option2)
        self.memo[(idx1, idx2)] = result
        return result

s = Solution()
print(s.longestPalindromeSubseq("aababaaa", 0, None))