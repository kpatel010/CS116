def is_composite(n, d):
  '''
  Returns True if any number between 2 and d 
  divides n and False otherwise
  
  is_composite: Nat Nat -> Bool
  Requires: 
     2 <= n
     1 <= d <= n-1
  '''
  if d == 1:
    return False 
  elif (n % d) == 0:
    return True
  else:
    return is_composite(n, d - 1)
    
def is_prime(n):
  '''
  Returns True if n is prime and false otherwise.
  
  is_prime: Nat -> Bool
  '''
  if n <= 1:
    return False 
  return not(is_composite(n, n-1))
  
def sqaurefree(n, d):
  '''
  Returns True if n is squarefree and false otherwise
  
  sqaurefree: Nat Nat -> Bool
  Requires: 
     2 <= n
     1 <= d <= n-1
  ''' 
  if d == 1:
    return True 
  if is_prime(d) == True:
    if ((n % (d ** 2)) == 0) and (n % d == 0):
      return False
    else:
      return sqaurefree(n, d - 1)
    if (n % d == 0):
      return True 
    else:
      return sqaurefree(n, d - 1)
  else:
    return sqaurefree(n, d - 1)

def count_primes(n, d):
  '''
  Returns the number of prime factors of n
  
  count_primes: Nat Nat -> Nat 
  Requires: 
     2 <= n
     1 <= d <= n-1
  '''
  if d == 1:
    return 1 
  else:
    if sqaurefree(n, d) == True:
      return 1 + sqaurefree(n, d - 1)
      
def mobius(n):
  '''
  Returns 0 if n is not squarefree, 1 if n has an even number of prime 
  factors and -1 if n has an odd number of prime facotrs 
  
  mobius: Nat -> (anyof -1 0 1)
  Requires 
    Nat > 0
  
  Examples:
    mobius(12) => 0
    mobius(6) => 1
    mobius(10) => -1
  '''
  if n == 1:
    return 1
  if is_prime(n) == True:
    return -1
  elif sqaurefree(n, n - 1) == False:
    return 0 
  elif count_primes(n, n - 1) % 2 == 0:
    return 1
  elif count_primes(n, n - 1) % 2 == 1:
    return -1 