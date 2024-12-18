# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    answer.append(prices[i] - prices[j])
                    break
                if j == len(prices) - 1:
                    answer.append(prices[i])
            if i == len(prices) - 1:
                answer.append(prices[i])
        return answer
