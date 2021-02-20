invalid_text = "Invalid IP address"
input_prompt = "Enter a valid IPv4 number: " 

def valid_input(x):
  '''
  Returns a boolean depending on if x is considered a valid IPv4 address
  
  valid_input: Str -> Bool
  
  Effects:
     Reads input from keyboard
  
  Examples:
  valid_input('111.111.111.111') => True
  if the string given by the user is considered a valid IP address
  
  valid_input('krishna') => False
  if the string given by the user is an invalid IP address 
  '''
  find = x.find('.')
  a = x[0:find]
  b = x[find + 1:x.find('.', find + 1)]
  c = x[x.find('.', find + 1) +1:x.rfind('.')]
  d = x[x.rfind('.') + 1:]
  
  if 7 <= len(x) <= 15 and x.count('.') == 3:
    if a.isnumeric() == True and b.isnumeric() == True and \
    c.isnumeric() == True and d.isnumeric() == True and \
    (0 <= int(a) <= 255) and (0 <= int(b) <= 255) and \
    (0 <= int(c) <= 255) and (0 <= int(d) <= 255):
      return True
    else:
      return False 
  else:
    return False

    
def cond_1(x):
  '''
  Returns a boolean depending on if x is considered a valid hacker
  IP address based on the first condition, that the first and last digit of
  the IP address is the same
  
  cond_1: Str -> Bool
  
  Effects:
     Reads input from keyboard
  
  Examples:
  cond_1('231.3.193.2') => True
  if the string given by the user is considered a valid IP address and meets
  the first condition 
  
  
  cond_1('4.123.23.3') => False
  if the string given by the user is considered a valid IP address and does 
  not meet the first condition
  '''
  if valid_input(x) == True:
    if x[0] == x[-1]:
      return True 
    else:
      return False 
  else:
    return False 
      
def cond_2(x):
  '''
  Returns a boolean depending on if x is considered a valid hacker
  IP address based on the second condition, that any of a,b,c,d when
  reversed is one of the other values in a,b,c,d.
  
  cond_2: Str -> Bool
  
  Effects:
     Reads input from keyboard
  
  Examples:
  cond_2('123.45.54.198') => True
  if the string given by the user is considered a valid IP address and meets
  the second condition
  
  cond_2('110.11.9.123') => True
  if the string given by the user is considered a valid IP address and does 
  meet the second condition
  
  cond_2('1.1.34.235) => False 
  if the string given by the user is considered a valid IP address and does 
  not meet the second condition
  '''
  find = x.find('.')
  a = x[0:find]
  b = x[find + 1:x.find('.', find + 1)]
  c = x[x.find('.', find + 1) +1:x.rfind('.')]
  d = x[x.rfind('.') + 1:]
  
  if valid_input(x)==True:
    if a.strip('0')==(b[::-1]).strip('0') or (a[::-1]).strip('0')==b.strip('0')\
    or a.strip('0')==(c[::-1]).strip('0') or (a[::-1]).strip('0')==c.strip('0')\
    or a.strip('0')==(d[::-1]).strip('0') or (a[::-1]).strip('0')==d.strip('0')\
    or b.strip('0')==(c[::-1]).strip('0') or (b[::-1]).strip('0')==c.strip('0')\
    or b.strip('0')==(d[::-1]).strip('0') or (b[::-1]).strip('0')==d.strip('0')\
    or d.strip('0')==(c[::-1]).strip('0') or (d[::-1]).strip('0')==c.strip('0'):
      return True
    else:
      return False
  else:
    False
    
def almost_hacker(i):
  '''
  Reads in a string from the keyboard and determines if the string meets the 
  criteria for a hacker IP address. If IP address is considered to be a hacker, 
  will return True. If a valid IP address was inputted, function will return 
  False. Any other inputs will return None. 
  If IP address is invalid, user will have a total of i attempts of inputting 
  a valid IP address
  
  Effect:
    Reads input from keyboard
    Prints 'Invalid IP address' if user input is invalid, if user input is valid
    nothing happens 
    This process is repated i times
  
  almost_hacker: Str -> (anyof Bool None) 
  
  Examples:
  
  If the user enters '131.11.8.199', almost_hacker(4) => False 
  
  If the user enters '11.011.12.2' when almost_hacker(4) => True
       
  If the user enters "hello" when almost_hacker(4) is called, None is returned. 
  'Invalid IP address' is printed. User gets another attempt to input an IP
  address, to a total of i attempts 
  '''
  if i == 0:
    return None
    
  x = (input(input_prompt))
  
  if valid_input(x) == True and cond_1(x) == False and cond_2(x) == False:
    return False 
  if valid_input(x) == True and cond_1(x) == True or cond_2(x) == True:
    return True
  else:
    print(invalid_text)
    return (almost_hacker(i-1))
    almost_hacker(i - 1)
    
def hacker():
  number_of_attempts = 4
  '''
  Reads in a string from the keyboard and the user has four attempts to 
  input a IP address. Returns 'Invalid IP address' if user input is 
  not valid. Returns False if user input is a valid IP address. Returns True
  if input is considered a hacker IP address
  
  Effects: 
    Reads input from keyboard
    Prints 'Invalid IP address' if user input is invalid, if user input is valid
    nothing happens 
    This process is repated 4 times
    
  hacker: None -> (anyof Bool None)
  
  Examples: 
    If the user enters '1.1.1.1', hacker() => True
       
    If the user enters "patel", hacker() => None and  
    'Invalid IP address' is printed. User gets another attempt to input an IP
    address, to a total of four attempts 
  '''
  return almost_hacker(number_of_attempts)