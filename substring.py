class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        best = 0
        left = 0
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # 3
    print(solution.lengthOfLongestSubstring(""))          # 0
        