class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        # calculate the product of all elements to the left of each index
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        # calculate the product of all elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))    # [24, 12, 8, 6]
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))    # [0, 0, 9, 0, 0]