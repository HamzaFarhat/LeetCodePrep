class Solution(object):
    def rotate(self, nums, k):
        """
     1. i+k+1 
     2. need a temp array
        """
        
        newArray= list(nums)
        
        for i in range(0,len(nums)):
            newIndex = (i+k) % len(nums)
            newArray[newIndex] = nums[i]
            
        for i in range(0,len(nums)):
            nums[i] = newArray[i]
        
