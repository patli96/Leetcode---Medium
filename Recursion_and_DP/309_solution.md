## 309. Best Time to Buy and Sell Stock with Cooldown

### Description

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

**Example:**
```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

### Solution

For this problem, we are going to create tow arrays to represent two states - buy-in and selling.

Explanation of *i* th element in both array:
- **buy[*i*]** indicates the maximum profits at the end of day *i*, and the last action taken was buying in
- **sell[*i*]** indicates the maximum profits at the end of day *i*, and the last action taken was selling


According to the description of this problem, we can know that:
- After a buy-in action, we can choose to hold or sell;
- After a selling action, we can choose to buy in new stocks after at least an one-day cooldown or just hold our profits

So in this way, for the ```buy``` array, ```buy[i]``` could be:
- **```buy[i-1]```**: hold the profits from day *i-1*
- **```sell[i-2] - prices[i]```**: buy in new stocks on day *i* with the price of ```prices[i]```, based on the profits from ```sell``` array on day *i-2* followed by a cooldown on day *i-1*, in case there was a selling action on day *i-2*

For the ```sell``` array, ```sell[i]``` could be:
- **```sell[i-1]```**: hold the profits from day *i-1*
- **```buy[i-1] + prices[i]```**: selling the stocks on day *i* with the price of ```prices[i]```, based on the profits from ```buy``` array on day *i-1*

In summary:
```python
buy[i] = max(buy[i-1], sell[i-2] - prices[i])
sell[i] = max(sell[i-1], buy[i-1] + prices[i])
```

### Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) == 1:
            return 0
        
        ndays = len(prices)
        
        # initialize the two arrays
        buy = [None] * ndays
        sell = [None] * ndays
        
        buy[0] = -prices[0]
        buy[1] = max(-prices[1], buy[0])
        
        sell[0] = 0
        sell[1] = max(buy[0] + prices[1], sell[0])
        
        # traverse the prices list
        for i in range(2, ndays):
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
            
        return max(buy[-1], sell[-1], 0)
```