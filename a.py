def maxProfit( prices):
        """
        :type prices: List[int]
        :rtype: int
       """
        min_prince  = min(prices)
        print(min_prince)
        for index,prince in enumerate(prices):
            
            
            if prince == min_prince:
                index_min = index

        print(index_min)
        print(prices[index_min:])
        print(max(prices[index_min:]))
        print(min_prince)
        return max(prices[index_min:]) - min_prince 
            
prices = [2,4,1]
print(maxProfit(prices))      