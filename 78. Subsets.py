class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def select(c, cur, i):
            if len(cur) == c:
                res.append(list(cur))
                return
            if i >= len(nums):
                return
            cur.append(nums[i])
            select(c, cur, i + 1)
            cur.pop()
            select(c, cur, i + 1)

        for j in range(len(nums) + 1):
            select(j, [], 0)
        return res
