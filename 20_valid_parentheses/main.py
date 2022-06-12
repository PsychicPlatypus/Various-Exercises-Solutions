import re

class Solution(object):
    def isValid(self, string):
        stack = []
        for i in string:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if len(stack) == 0:
                    return False
                if (i == ')' and stack[-1] == '(') or\
                    (i == '}' and stack[-1] == '{') or\
                    (i == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

test = Solution()

print(test.isValid("12+(3+4)+5)+3(2"))