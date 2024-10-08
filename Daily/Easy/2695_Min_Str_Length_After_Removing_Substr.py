# My Initial Solution
class Solution:
    def minLength(self, s: str) -> int:
        check = True

        while check:
            if "AB" in s and "CD" in s:
                s = s.replace("AB", "")
                s = s.replace("CD", "")
            elif "AB" in s: 
                s = s.replace("AB", "")
            elif "CD" in s:
                s = s.replace("CD", "")
            else:
                check = False
        return len(s)



### Revised Solution
class Solution:
    def minLength(self, s: str) -> int:
        # Stores the char that are not being removed
        stack = []
       
        # Iterate through given str
        for x in s:
            # "and stack" ensures you are only removing if there are elements in stack
            # Remove the end of stack (i.e previous char A) if the next char is B 
            if x == 'B' and stack and stack[-1] == 'A': 
                stack.pop()
            # Remove the end of stack (i.e previous char C) if the next char is D
            elif x == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            # Add char to the stack
            else:
                stack.append(x)
    
        return len(stack)     
