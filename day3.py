1.
import datetime
 
print("##### Welcome to age calculator ######")

birth_year = int(input("Enter your year of birth: \n"))

current_year = datetime.date.today().year

age_year = current_year - birth_year

print("Your exact age is: ", age_year, "Years")

2.
x = input("Type  number one : ")
y = input("Type  number two : ")

add = int(x) + int(y)
sub = int(x) - int(y)
div = int(x) / int(y)
div2 = int(x) // int(y)
mul = int(x) * int(y)
rem = int(x) % int(y)
pow = int(x) ** int(y)

print("The addition is: ", add)
print("The substraction is: ", sub)
print("The division1 is: ", div)
print("The division2 is: ", div2)
print("The multipliction is: ", mul)
print("The remainder is: ", rem)
print("The power is: ", pow)

3.
string = "eduyearyesaryyreayye"
substring = "y"
count = string.count(substring)
print("The count is:", count)

4.
str = input("Enter a string\n")
# create a string with characters at multiples of 2
modified_string = str[::2]
print(modified_string)

