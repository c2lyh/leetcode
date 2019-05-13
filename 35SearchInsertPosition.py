'''
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0



'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = int((left + right) / 2)

            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid
        return left






'''
#Solution1: 我的智障方式

class Solution:
    def searchInsert(self, nums, target):

        if target in nums:
            print("yes its in")

            print(nums.index(target))
            return (nums.index(target))

        else:
            for i in range(len(nums)):
                print("in the loop")
                print(i)

                if nums[i] > target:
                    print('here we go')
                    print(i)

                    return i

            return len(nums)


'''


if __name__ == '__main__':
    num1 = [1,3,5,6]
    target1 = 5
    num2 = [1,3,5,6]
    target2 = 2



    A = Solution()
    A.searchInsert(num2,target2)

