class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  # return valid bounds

        for i in range(len(s)):
            # Odd-length palindrome
            l1, r1 = expand_around_center(i, i)
            # Even-length palindrome
            l2, r2 = expand_around_center(i, i + 1)
            
            # Choose the longer one
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]