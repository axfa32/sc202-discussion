class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        #for i in range(len(nums)):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[left] = nums[i]
                left+=1
        return left
