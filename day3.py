1.

import datetime
 
print("##### Welcome to age calculator ######")

birth_year = int(input("Enter your year of birth: \n"))

current_year = datetime.date.today().year

age_year = current_year - birth_year

print("Your exact age is: ", age_year, "Years")

2.
