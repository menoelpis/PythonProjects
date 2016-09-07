def is_leap_year(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False


year = input("Enter the year: ")
result = is_leap_year(int(year))

if result == True:
  print("Year " + year + " is a leap year.")
else: 
  print("Year " + year + " is not a leap year.")
   