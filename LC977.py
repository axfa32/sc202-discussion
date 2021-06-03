class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_num=len(nums)
        x=0
        y=len_num-1
        output=[0]*len_num
        for i in range(len_num-1,-1,-1):
            if abs(nums[x]) < abs(nums[y]):
                output[i]=nums[y]*nums[y]
                y -= 1
            else:
                output[i]=nums[x]*nums[x]
                x += 1
        return output
