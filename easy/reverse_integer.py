"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x: int) -> int:
        reversed = str(x)[::-1]
        if reversed.endswith("-"):
            reversed = "-" + reversed[:-1]
        reversed = int(reversed)
        if reversed > (2**31-1) or reversed < -2 **31:
            reversed = 0
        return reversed


if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(1534236469))

