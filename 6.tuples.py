# Tuples are immutable
tuple = (2,34,5,5)

print(type(tuple))


# Write a code to check palindrome
list1 = [1,3,3,1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

