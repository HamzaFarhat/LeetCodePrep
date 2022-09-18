class Solution(object):
    def removeDuplicates(self, nums):
        """
        1. Have 2 pointers, compare index 0 and 1
        2. if they are the same, keep increminting one pointer its the same value
        3. pointer a is OG value, pointer b should be the new number
        5. return a+1
        """
        
        
        a=0 #unique elements 
        b=0 #loops to find duplicates 
        
        while b < len(nums):
            if nums[a] == nums[b]:
                b = b+1
                
            else:
                a = a+1 
                nums[a] = nums[b] 
                b = b+1                
                
        return a+1
        
