from typing import List

"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        max_profit = 0

        prices.reverse()

        for value in prices:
            max_value = max(value, max_value)
            profit = max_value - value
            max_profit = max(profit, max_profit)

        return max_profit


def test_base_case():
    assert_are_equal(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

def all_decreasing():
    assert_are_equal(Solution().maxProfit([7, 6, 5, 4, 3, 1]), 0)

def assert_are_equal(actual, expected):
    assert actual == expected, f"Expected: '{expected}' but got '{actual}'"

if __name__ == '__main__':
    test_base_case()
    all_decreasing()
