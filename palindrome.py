import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        num_digits = int(math.log10(x)) + 1
        while num_digits > 1:
            power_of_ten = num_digits - 1
            first_digit = x // (10 ** power_of_ten)
            print(f"First digit is {first_digit}")
            last_digit = x % 10
            print(f"Last digit is {last_digit}")
            if first_digit != last_digit:
                return False
            # remove first digit
            x = x - first_digit * (10 ** power_of_ten)
            print(f"Removed first digit: {x}")
            # remove last digit
            x = x // 10
            print(f"Removed last digit: {x}")
            num_digits -= 2
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121),"\n")
    print(solution.isPalindrome(-121),"\n")
    print(solution.isPalindrome(10),"\n")
    print(solution.isPalindrome(1234321),"\n")
    print(solution.isPalindrome(12344321),"\n")
    print(solution.isPalindrome(1000021),"\n")
