class Solution(object):
    def moveZeroes(self, nums):
         
        a=0 # the non 0 index  
        b=0 # the 0 index to swap with the non 0 index 
        
        while a < len(nums):
            if nums[a] == 0:
                a += 1
            elif nums[a] != 0:
                nums[a], nums [b]= nums[b], nums[a]
                a += 1
                b += 1
