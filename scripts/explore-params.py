# This file contains the PPCG parameter values that are explored.
# The exploration script considers each combination of the parameter values.

([
  # Tile sizes
  ['1,1', '1,2', '1,4',
   '2,1', '2,2', '2,4',
   '4,1', '4,2', '4,4', '4,8',
           '8,4', '8,8',
   '8,16', '16,8',
   '16,16',
   '32,16', '16,32', '64,64'],

  # Grid sizes
  ['16,16', '32,32', '256,256', '1024,1024'],

  # Block sizes
  ['1,1', '1,2', '1,4', '1,8',
   '2,1', '2,2', '2,4', '2,8',
   '2,16',
   '4,1', '4,2', '4,4', '4,8',
   '4,16',
   '8,1', '8,2', '8,4', '8,8',
   '8,16',
   '16,16', '32,32', '64,64']
])
