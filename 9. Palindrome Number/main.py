class Solution(object):
    def isPalindrome(self, x):
        if(x == x[::-1]):
            return True
        return False
