1.
vowels=['a','e','i','o','u']
word='abed'
for i in word:
    if i in vowels:
                print(word.index(i))

2.
## initializing the string
string = "hello world happy birthday"
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
print(" ".join(words))

3.
a = [1, 2, 3, 3, 2, 4]
b = []
for i in a:
    # Add to the new list
    # only if not present
    if i not in b:
        b.append(i)
print(b)
