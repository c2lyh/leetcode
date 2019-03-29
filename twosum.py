
#o(n^2)  since its 2D loop
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i]+nums[j]
            if sum == target:
                print(i,j)
                return [i,j]



                
#0(n) loop only once by storing shits in dictionary
def dicway(nums,target):

    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            print ([dic[target - nums[i]],i] )
            return [dic[target - nums[i]],i]
        if nums[i] not in dic:
            dic[nums[i]] = i







if __name__ == "__main__":
    #twoSum([2, 7, 11, 15],9)
    dicway([2, 7, 11, 15],9)

