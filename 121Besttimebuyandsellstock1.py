class Solution:
    def maxProfit(self, prices) -> int:



        maxprofit, minprice = 0,float('inf')

        for price in prices:

            minprice = min(minprice, price) #minprice to hold the lowest price when compare ith element
            maxprofit = max(maxprofit, price - minprice) #maxprofit holds the largest difference between previous elements and
                                                        #next elements

        print(maxprofit)
        return maxprofit






    #learned from michell (youtuber)



if __name__ == '__main__':
    a = Solution()
    e1 = [7,1,5,3,6,4] #5
    e2 = [7,6,4,3,1] #0

    a.maxProfit(e1)
    a.maxProfit(e2)



'''

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''