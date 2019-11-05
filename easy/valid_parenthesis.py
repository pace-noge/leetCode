"""
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        if len(s) == 0:
            return True
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack = []
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if (len(stack) > 0) and (open_list[pos] == stack[len(stack) -1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True


if __name__ == "__main__":
    test_case = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True)
    ]
    solution = Solution()
    for case in test_case:
        success = solution.isValid(case[0]) == case[1]
        print(f"Input: {case[0]}")
        print(f'Output: {success}')
