class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
     
        # Determine the sum of given array 
        s = sum(nums)
        answer = 0

        # Check if sum of nums is divisible by p
        if s % p == 0:
            return answer

        # If sum is not divisible by find subarrays
        else:
            length = len(nums)
            while length >= 0:
                subs = combinations(nums, length - 1)
                answer += 1
                length -= 1
                
                # Iterate through subarrays to check if its sum is divisible by p
                for sub in subs:
                    new_s = sum(sub)
                    
                    # Return the number of elements that was needed to be removed, else return -1 
                    if new_s % p == 0:
                        return answer
            return -1
                        

