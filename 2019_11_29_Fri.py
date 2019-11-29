'''
Leetcode 
figuring out the existence of duplicates
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    

'''
LeetCode 
Return value that only appears once. 
'''
class Solution: # find a value that only comes once. Others come twice. 
    def singleNumber(self, nums: List[int]) -> int:
        tmp = set({}) # empty set
        for num in nums:
            if num in tmp:
                tmp.remove(num)
            else:
                tmp.add(num)
                
        return list(tmp)[0]
        
