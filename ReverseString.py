class Solution(object):
    def reverseString(self, s):
        
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # parse through each index in the letters
        # can start from index n and go to index 0
        # take the last string and place to first index 0 in second array 
        # this takes O(n) memory space 
        
        # 2 POINTER APPROACH 
        # start at index 0 
        # 2nd pointer at index n
        # swap pointer 1 with pointer n 
        
        l = 0
        r = len(s) - 1 
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l = l+1 
            r = r-1 
