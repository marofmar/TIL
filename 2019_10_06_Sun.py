'''
TIL Sun 6 Oct 
1. 
The rules of giving bonuses is that:
- Each employee begins with a bonus factor of 1x.
- For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).

Given a list of employee's performance, find the bonuses each employee should get.

Example:
Input: [1, 2, 3, 2, 3, 5, 1]
Output: [1, 2, 3, 1, 2, 3, 1]
'''
def getBonuses(perf):
  # Fill this in.
	count = len(perf)
	bonus = [1] * count # initialize bonus 1 for everyone 

	for i in range(1, count):
		if perf[i-1] < perf[i]: # first left to right
			bonus[i] += 1
	#print(bonus)
	for i in range(count-2, 1, -1):
		if perf[i+1] < perf[i]:
			bonus[i] +=1
	print(bonus)
	return bonus




#print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]

'''
2. 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
class Solution:
    def isValid(self, s: str) -> bool: # same, order 
        # recursive 
        stack = [] 
        l = ['(','{','[']
        r = [')','}',']'] # same value, and same order 
        #d = {'{':'}', '(':')','[':']'} 
        d = {'}':'{',')': '(',']':'['}
        for i in s:
            if i in d: # calling a key in d
            	#print(i)
                if stack: # if sth is in stack 
                    top_element = stack.pop() # remmove 
                else:
                    top_element = '#' # dummy..? why?
                if d[i] != top_element: # if the value is not the pair, 
                    return False 
            else:
                stack.append(i)
            if i not in d:
            	stack.append(i)
            else:
            	if stack:
            		top_element = stack.pop() 
        return not stack
                
            
        
  


            
        



