from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int, verbose: bool = False) -> List[int]:
        vprint = print if verbose else lambda *args, **kwargs: None

        vprint("Received arguments:")
        vprint(f"nums: {nums}")
        vprint(f"target: {target}")
        vprint("After enumerating")
        vprint(list(enumerate(nums)))

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            vprint(f"Current index: {i}, Current number: {num}, Complement: {complement}")
            if complement in seen:
                vprint(f"Complement {complement} found in seen with index {seen[complement]}")
                return [seen[complement], i]
            else:
                vprint(f"Complement {complement} not found in seen. Adding {num} to seen with index {i}")
            seen[num] = i
            vprint(f"Seen dictionary: {seen}\n")
        
        vprint("No solution found.")
        return[-1, -1]  # Return an invalid index pair if no solution is found


if __name__ == "__main__":
    solution = Solution()
    i, j = solution.twoSum([2, 7, 11, 15], 9, verbose=True)
    print(f"\nSolution indices: {i}, {j}")
