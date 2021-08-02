class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def helper(s, i, currstr):
            if i == len(s):
                result.append(currstr)
            else:
                if s[i].isalpha():
                    helper(s, i+1, currstr+s[i].lower())
                    helper(s, i+1, currstr+s[i].upper())
                else:
                    helper(s, i+1, currstr+s[i])
            helper(s, 0, "")
            return result
