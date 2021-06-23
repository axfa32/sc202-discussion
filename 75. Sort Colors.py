class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

                #youtube: https://www.youtube.com/watch?v=sEQk8xgjx64
                #dutch partitioning problem
                #substitute red,white,blue to low,med,high, for better visualization.
