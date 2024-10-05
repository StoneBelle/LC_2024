class Solution:
  def dividePlayers(self, skill: List[int]) -> int:
      
      # Check if given list has length of two 
      length = len(skill)
      pairs = int(length / 2)

      if length == 2:
          return skill[0] * skill[1]

      # Divide the players into teams of even skill 
      ordered_skills = sorted(skill)
      first_half = ordered_skills[0:3]
      second_half = ordered_skills[length-1:-(length-pairs + 1):-1]

      teams = tuple(zip(first_half, second_half)) 

      chem = 0
      x = []
      for team in teams:
          x.append(math.prod(team))
          chem += math.prod(team)
      
      y = Counter(x)
      if len(y) > 1 :
          return -1
      else:
          return chem
