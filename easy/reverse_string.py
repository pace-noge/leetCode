

class Solution:
    def reverse_string(self, s: list) -> None:
        """
        :type s: List[str]
        :rtype:None Do not return anything, modify s in place instead
        """
        if len(s) == 0 or s is None:
            return s
        return self.reverse_string(s[1:]) + list(s[0])



if __name__ == "__main__":
    s = list("hello")
    solution = Solution()
    print(solution.reverse_string(s))
    s = ["H","a","n","n","a","h"]
    print(solution.reverse_string(s))



