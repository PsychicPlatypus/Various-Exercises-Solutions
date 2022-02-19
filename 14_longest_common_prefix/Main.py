class Solution(object):
    def longestCommonPrefix(self, strs):
        longest_prefix, counter, keep_going = "", 0, True
        while keep_going:
            try:
                current_letter = strs[0][counter]
                for i in strs:
                    if i[counter] != current_letter:
                        keep_going = False
                        print(strs[len(strs)+1])
                longest_prefix += current_letter
                counter += 1
            except(IndexError):
                keep_going = False
        return longest_prefix
    

test = Solution()
print(test.longestCommonPrefix(["flower","flow","flight"]))