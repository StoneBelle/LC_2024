from collections import Counter
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # Create a sorted copy of the given array without duplicated elements
        ordered_items = Counter(sorted(arr))
        my_keys = ordered_items.keys()
    
        # Assign a rank to each of the integers
        rank = 1
        all_ranks = []
        for key in my_keys:
            all_ranks.append(rank)
            rank += 1

        x = dict(zip(my_keys, all_ranks))

        # Return an array containing the rank of each integer in the given array
        answer = []
        for a in arr:
            f_rank = x.get(a)
            answer.append(f_rank)

        return answer


