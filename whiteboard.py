class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def helper(lst):
            if i == len(s):
                result.append("".copylist)
            else:
                if s[i].isalpha():
                    helper(s[i+1].lower())
                    helper(s[i+1].upper())
                else:
                    helper(s, i+1, currstr+s[i])
            helper(list(s))
            return result
