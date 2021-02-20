def unicode_encoding(s):
  '''
  Return the correct UTF-8 binary encoded string dependant on s
  
  unicode_encoding: Str -> Str 
  Requires:
    0 < len(s) < 21
    S inputted into unicode_encoding will either be '0' or 
    have a leftmost digit of '1'
    S can have either digits '1' or '0'
  
  Examples:
  unicode_encoding('101001') => '00101001'
  unicode_encoding('11101001') => '1100001110101001'
  '''
  if len(s) == 7 or len(s) == 11 or len(s) == 16 or len(s) == 21:
    return s
  if len(s) < 7:
    return '0' * (8 - len(s)) + s 
  elif 7 < len(s) < 11:
    return '110' + ('0' * (11 - len(s)) + s)[:5] + '10' \
          + ('0' * (11 - len(s)) + s)[5:]
  elif 11 < len(s) < 16:
    return '1110' + ('0' * (16 - len(s)) + s)[:4] + '10' + \
          ('0' * (16 - len(s)) + s)[4:10] + '10' + \
          ('0' * (16 - len(s)) + s)[10:]
  else:
    return '11110' + ('0' * (21 - len(s)) + s)[:3] + '10' + \
          ('0' * (21 - len(s)) + s)[3:9] + '10' + \
          ('0' * (21 - len(s)) + s)[9:15] + '10'\
          + ('0' * (21 - len(s)) + s)[15:]