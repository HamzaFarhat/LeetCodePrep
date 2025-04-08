# LeetCodePrep
- Some of my Leetcode solutions from daily practice 

### To include Advanced Algorithms, Data Structures, Leetcode 150 (Neetcode)
# Arrays
## Remove Duplicate 
- Uses O(1) memory space and a 2 pointer approach to solve question 
## Sol.py 
- Best Time to Buy and Sell Stock II Solution
## Rotate.py
- Rotate index in array by value k (O(n) memeory space, makes use of second array) 
## ContainsDuplicate.py
- Used sets to find theres no duplicates, just solved in one line as original list cannot equal to set(), if unequal theres a duplicate in the list, returns false 
## SingleNumber.py
- Needs O(1) Space complexity, used XOR bit minipulation, the remainder is always the unique element .Used another list and popped from it. Howeveer, O(n)
## MoveZereos.py
- used 2 pointer approach, one is non zero, other is zero. swap values, incerement both
## TwoSum.py
- O(n^2) time complexity, 2 pointer approach may also be used here 
## ValidAnagram.py
- two different solutions O(1) memory is using bubble sort "sorted()" function built in on python. Also O(n) memory is comparing 2 dictionaries (key, value) pairs 
## RotateImage.py
- Used matrices, rotate from one point to other 
## Find difference between 2 programmers (Hackerrank) 
- used a simple while loop to find how many days for one person to catch up to another to solve problems. Find edge cases
## Hashmap
Find key value pairs using hash map

# Strings 
## ReverseString.py 
- O(n^2) time complexity, 2 pointer approach from opposite ends, instead o brute first and using .reverse() function in python
