from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for cur_str in strs:
            sorted_key = tuple(sorted(cur_str))
            groups[sorted_key].append(cur_str)
        return list(groups.values())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
