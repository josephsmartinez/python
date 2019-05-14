# Time Complex: O( N * N )
def balancedAB(string):
  for i in range(0 , len(string)):
    if ord(string[i]) == 66 and i+1 < len(string):
      for j in range(i , len(string)):
        if ord(string[j]) == 65 and j < len(string):
          return False
  return True  
