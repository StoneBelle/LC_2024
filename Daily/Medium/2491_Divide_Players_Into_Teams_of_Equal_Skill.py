import math 
from collections import Counter
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        length = len(skill) # Length of given array 
        pairs = int(length / 2) # Total number of teams 

        # Check if given array has only 1 team
        if length == 2:
            print( skill[0] * skill[1])

        # Sort given array and create teams of even skill
        ordered_skills = sorted(skill) 
        first_half = ordered_skills[0:3] # Slices front half of array 
        second_half = ordered_skills[length-1:-(length-pairs + 1):-1] # Slices end half of array, reverse order
        teams = tuple(zip(first_half, second_half)) # Pairs players into even teams

        chem = 0 # Stores chemistry sum
        x = [] # Store the sum of each team's skill
        for team in teams:
            x.append(sum(team))
            chem += math.prod(team) # Updates cumulative team chemistry

        y = Counter(x) # Counts the freq of each team sum
        if len(y) > 1:
            return -1
        else:
            return chem
