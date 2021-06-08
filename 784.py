class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res=[]
        self.dfs(S,'',0, res)
        return res

    def dfs(self,S,path,index, res):
        if index==len(S):
            res.append(path)            
            return

        if S[index].isalpha():
            self.dfs(S,path+S[index].lower(),index+1, res)
            self.dfs(S,path+S[index].upper(),index+1, res)
        else:
            self.dfs(S,path+S[index],index+1, res)
