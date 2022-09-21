class Solution(object):
    def twoSum(self, nums, target):

        '''
        1. find the value of index a and index b 
        2. check what both values add to 
        3. if adds to target stop running
        4, if it doesnt keep moving index b, but stay at index a
        5. just append both
        '''
        
        for i in range(0, len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
                            
