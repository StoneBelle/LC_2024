##
class Solution:
    def minimumSteps(self, s: str) -> int:
        # TWO POINTER APPROACH

        l_pointer = 0 # Focuses on keeping white balls on the leftside 
        min_swaps = 0 # Keeps track of swaps

        # r_pointer will iterate through each char in given str
        for r_pointer in range(len(s)):
            # Checks if the char is a "0" or "1"
            if s[r_pointer] == "0":
                min_swaps += (r_pointer - l_pointer) # Difference between r & l will be added to min_swaps
                l_pointer += 1 # Ensures white balls on leftside

            # else statement is not required since we focus on "0", not "1"

        return min_swaps
