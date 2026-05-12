class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram")) # True
    print(solution.isAnagram("car", "rat"))         # False
    print(solution.isAnagram("a", "a"))             # True  — single char, same
    print(solution.isAnagram("a", "b"))             # False — single char, different
    print(solution.isAnagram("aa", "bb"))           # False — same length, no overlap
    print(solution.isAnagram("aab", "bba"))         # False — catches count overflow
    print(solution.isAnagram("", ""))               # True  — empty strings

