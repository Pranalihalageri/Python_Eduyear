1.

list1 = [5, 20, 4, 45, 66, 93, 1]  
even_count, odd_count = 0, 0
# iterating each number in list
for num in list1:
      
    # checking condition
    if num % 2 == 0:
        even_count += 1
  
    else:
        odd_count += 1
          
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

2.
list1 = [10, 20, 4, 45, 99]
  
# sorting the list
list1.sort()
  
# printing the last element
print("Largest element is:", list1[-1])
print("minimum element is:", *list1[:1])
