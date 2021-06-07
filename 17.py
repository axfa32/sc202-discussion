class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map=["0","1","abc","def","ghi", "jkl","mno","pqrs","tuv","wxyz"]
        
        res=[]
        if len(digits)==0:
            return res
        res.append("")
        for digit in digits:
            tmp=list()
            chars=map[int(digit)]
            for r in res:
                for char in chars:
                    tmp.append(r+char)
            res=tmp
        return res
