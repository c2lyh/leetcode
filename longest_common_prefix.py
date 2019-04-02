'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ''

        min_str = min([len(i) for i in strs])
        prefix = ''
        for index in range(min_str):
            if len(set([j[index] for j in strs])) == 1:
                prefix += strs[0][index]
            else:
                break
        print(prefix)
        return prefix


if __name__ == '__main__':
    b = ["flower", "flow", "flight"]

    a = Solution()
    a.longestCommonPrefix(b)



