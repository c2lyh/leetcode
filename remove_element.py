class Solution:
    def removeElement(self, A, elem):
        j = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j + 1







if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    a = Solution()
    a.removeElement()
