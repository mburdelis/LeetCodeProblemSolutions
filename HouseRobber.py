from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        bestUntilPrevious = 0
        bestUntilCurrent = 0

        for num in nums:
            newBest = max(bestUntilCurrent, bestUntilPrevious + num)
            bestUntilPrevious = bestUntilCurrent
            bestUntilCurrent = newBest

        return bestUntilCurrent


if __name__ == "__main__":
    solution = Solution()

    assert solution.rob([10, 1, 1, 10]) == 20       # basic: skip index 1 and 2, take 0 and 3
    assert solution.rob([1, 2, 3, 1]) == 4       # basic: skip index 1, take 0+2
    assert solution.rob([2, 7, 9, 3, 1]) == 12   # basic: take index 0, 2, 4
    assert solution.rob([0]) == 0                 # single house, zero value
    assert solution.rob([5]) == 5                 # single house
    assert solution.rob([1, 2]) == 2              # two houses, take the larger
    assert solution.rob([2, 1]) == 2
    assert solution.rob([0, 0, 0]) == 0           # all zeros
    assert solution.rob([100, 1, 100]) == 200     # skip middle

    print("All tests passed!")
