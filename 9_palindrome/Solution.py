from re import S


class Solution(object):
    def isPalindrome(self, x):
        j = [i for i in str(x)]
        j.reverse()
        return str(x) == "".join(j)
        
        
    
    
test = Solution()
test.isPalindrome(123)
        
        