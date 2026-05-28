from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums) # total number of 1s, which is the size of the window we need to fill with 1s
        doubled = nums + nums  # handle circular wrap-around

        window_ones = sum(doubled[:k])
        max_ones = window_ones

        for i in range(k, len(doubled)): # slide the window across the doubled array, counting 1s in each window of size k
            window_ones += doubled[i]
            window_ones -= doubled[i - k]
            max_ones = max(max_ones, window_ones)

        return k - max_ones # number of 1s we need to swap in is the total 1s minus the max 1s we can get in a window


if __name__ == "__main__":
    s = Solution()

    # LeetCode test cases
    print(s.minSwaps([0, 1, 0, 1, 1, 0, 0]))  # Expected: 1
    print(s.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))  # Expected: 2
    print(s.minSwaps([1, 1, 0, 0, 1]))  # Expected: 1
