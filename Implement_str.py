class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):  # 意思是最多遍历  len(haystack) 5 - len(needle) 2  = 3 +1 0,1,2,3
                                                          # 要流出len（needle）的范围
            print(i)
            if haystack[i:i + len(needle)] == needle:  # haystack[2:4] =ll


                return i  # i 为 0 的时候， haystack[0:0] 表示为 0
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    #should return 2: the index of first needle



    a = Solution()
    a.strStr(haystack,needle)




'''
Lazy way by using python library
#Solution1:
    
    
    return haystack.find(ll)
    
    or 
    
    
    return haystack.index(needle)
    
    Runtime: 48 ms, faster than 34.52% of Python3 online submissions for Implement strStr().
Memory Usage: 13.5 MB, less than 5.13% of Python3 online submissions for Implement strStr().
'''

'''
#Solution2:
#思路，用切片做循环比较
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):  # 有效减少比较的次数 #**不懂为什么要len(h)-len(n) +1 -> 5-2+1 = 4 0,1,2,3
            print(i)
            if haystack[i:i + len(needle)] == needle:  # haystack[2:4] =ll


                return i  # i 为 0 的时候， haystack[0:0] 表示为 0
        return -1

Runtime: 52 ms, faster than 27.97% of Python3 online submissions for Implement strStr().
Memory Usage: 13.4 MB, less than 5.13% of Python3 online submissions for Implement strStr().

wtf this one is even slower

'''