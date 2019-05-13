class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.rstrip().split(' ')[-1])






if __name__ == '__main__':
    a = Solution()
    input = "Hello World"

    a.lengthOfLastWord(input)






'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

