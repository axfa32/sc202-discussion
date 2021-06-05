class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1   
        # return sorted(set(nums)) class Solution:
 class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsLength = len(nums)
        
        if numsLength == 0:
            return 0
        
        left = 0
        right = 0
        output = 1
        
        while right < numsLength:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                output += 1
                nums[left] = nums[right]
                
        return output
    
