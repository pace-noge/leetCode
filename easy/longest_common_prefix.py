"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        strs.sort(key=len)
        min_s = strs.pop(0)
        pref = ""
        for i in range(len(min_s)):
            is_same = True
            for x in strs:
                if min_s[i] != x[i]:
                    is_same = False
                    break
            if not is_same:
                break
            else:
                pref += min_s[i]

        return pref



if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))

