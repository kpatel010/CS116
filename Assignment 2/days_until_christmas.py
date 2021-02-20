def days_until_christmas(day, month, year):
  '''
  Returns the number of days until Christmas according to day, month, year 
  and the Gregorian Calendar
  
  days_until_christmas: Nat Nat Nat -> Nat 
  Requires:
    Day, Month and Year must have values according to the Gregorian Calendar
    
  Examples:
    days_until_christmas(24, 12, 7574) => 1
    days_until_christmas(25, 12, 2019) => 0
    days_until_christmas(1, 1, 2020) => 359
  ''' 
  jan = 1
  feb = 2
  mar = 3
  apr = 4
  may = 5
  jun = 6
  jul = 7
  aug = 8
  sep = 9 
  octo = 10
  nov = 11
  dec = 12
  
  up = 31 
  down = 30 
  unique = 28
  
  number_of_days1 = (25 - day)
  number_of_days2 = (day - 25)
  
  if day == 25 and month == 12:
    return 0 
  if day < 25:
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
      if month == jan:
        return (up * 6) + (down * 4) + unique + number_of_days1 + 1
      elif month == feb:
        return (up * 5) + (down * 4) + unique + number_of_days1 + 1
      elif month == mar:
        return (up * 5) + (down * 4) + number_of_days1
      elif month == apr:
        return (up * 4) + (down * 4) + number_of_days1
      elif month == may:
        return (up * 4) + (down * 3) + number_of_days1
      elif month == jun:
        return (up * 3) + (down * 3) + number_of_days1
      elif month == jul:
        return (up * 3) + (down * 2) + number_of_days1
      elif month == aug:
        return (up * 2) + (down * 2) + number_of_days1
      elif month == sep:
         return up + (down * 2) + number_of_days1
      elif month == octo:
         return up + down + number_of_days1
      elif month == nov:
        return down + number_of_days1
      elif month == dec:
        return 25 - day
    else:
      if month == jan:
        return (up * 6) + (down * 4) + unique + number_of_days1
      elif month == feb:
        return (up * 5) + (down * 4) + unique + number_of_days1
      elif month == mar:
        return (up * 5) + (down * 4) + number_of_days1
      elif month == apr:
        return (up * 4) + (down * 4) + number_of_days1
      elif month == may:
        return (up * 4) + (down * 3) + number_of_days1
      elif month == jun:
        return (up * 3) + (down * 3) + number_of_days1
      elif month == jul:
        return (up * 3) + (down * 2) + number_of_days1
      elif month == aug:
        return (up * 2) + (down * 2) + number_of_days1
      elif month == sep:
        return up + (down * 2) + number_of_days1
      elif month == octo:
        return up + down + number_of_days1
      elif month == nov:
        return down + number_of_days1
      elif month == dec:
        return 25 - day
  if day >= 25 and month == 12:
    return days_until_christmas(0, 1, year + 1) + (31 - day)
  else:
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
      if month == jan:
        return (up * 6) + (down * 4) + unique - number_of_days2 + 1
      elif month == feb:
        return (up * 5) + (down * 4) + unique - number_of_days2 + 1
      elif month == mar:
        return (up * 5) + (down * 4) - number_of_days2
      elif month == apr:
        return (up * 4) + (down * 4) - number_of_days2
      elif month == may:
        return (up * 4) + (down * 3) - number_of_days2
      elif month == jun:
        return (up * 3) + (down * 3) - number_of_days2
      elif month == jul:
        return (up * 3) + (down * 2) - number_of_days2
      elif month == aug:
        return (up * 2) + (down * 2) - number_of_days2
      elif month == sep:
        return up + (down * 2) - number_of_days2
      elif month == octo:
        return up + down - number_of_days2
      elif month == nov:
        return down - number_of_days2
      elif month == dec:
        return day - 25
    else:
      if month == jan:
        return (up * 6) + (down * 4) + unique - number_of_days2
      elif month == feb:
        return (up * 5) + (down * 4) + unique - number_of_days2
      elif month == mar:
        return (up * 5) + (down * 4) - number_of_days2
      elif month == apr:
        return (up * 4) + (down * 4) - number_of_days2
      elif month == may:
        return (up * 4) + (down * 3) - number_of_days2
      elif month == jun:
        return (up * 3) + (down * 3) - number_of_days2
      elif month == jul:
        return (up * 3) + (down * 2) - number_of_days2
      elif month == aug:
        return (up * 2) + (down * 2) - number_of_days2
      elif month == sep:
        return up + (down * 2) - number_of_days2
      elif month == octo:
        return up + down - number_of_days2
      elif month == nov:
        return down - number_of_days2
      elif month == dec:
        return day - 25