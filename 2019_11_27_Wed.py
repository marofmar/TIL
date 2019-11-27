'''
LeetCode
Rotate Array
'''

class Solution:
  # list of integers: num (input)
  # number of steps to move: k(input)
  # return nothing, in place 
  def rotate(self, nums, k):
    n = len(nums)
    k = k%n
    nums[:] = nums[n-k:] + nums[:n-k]
