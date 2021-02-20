import math 

def iter_process(n, ite): 
  '''
  Returns the string of the integer values for the given continued fraction for
  n after the first iteration up until 0 iterations 
  
  iter_process: Float Nat -> Str 
  Requires:
    n > 0 
    n must be irrational 
  '''
  if ite == 0: 
    return "...]"
  else:
    step_1 = str(math.floor((n - (math.floor(n))) ** -1 ))
    return step_1 + "," + iter_process(((n - (math.floor(n))) ** -1), ite - 1)
    
def continued_fraction(n, iters): 
  '''
  Returns a string that represents the set of integer values for the given 
  continued fraction of n dependant on iters 
  
  contined_fraction: Float Nat -> Str 
  Requires:
    n > 0 
    n must be irrational
  
  Examples:
    continued_fraction(math.e, 12) => "[2;1,2,1,1,4,1,1,6,1,1,8,...]" \
    continued_fraction(math.pi + 2221, 1) => "[2224;...]"
    (continued_fraction(math.sqrt(83), 20)) => \
    "[9;9,18,9,18,9,18,8,1,1,2,25,1,29,1,1,7,1,1,1,...]"
  '''
  if iters == 1:
    return "[" + str(math.floor(n)) + ";...]"
  else:
    return "[" + str(math.floor(n)) + ";" + str(iter_process(n, iters - 1))