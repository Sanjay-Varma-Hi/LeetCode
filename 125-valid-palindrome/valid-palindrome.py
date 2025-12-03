class Solution(object):
    def isPalindrome(self, s):
        newstr = ''
        for i in s:
            if i.isalnum():
                newstr += i.lower()
        return newstr == newstr[::-1]
