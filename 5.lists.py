# lists are mutable means That can be changed
students = ["Tanush",10,"Saha",45.77]
students[1] = 43333
print(students[1])


# Slicing
print(students[0:2]) # Output : ["Tanush", 43333]


# list methods
list = [12,32,345,5454.434]
list.append(4)
print(list)


list.sort()  # Ascending Order
print(list)

list.sort(reverse=True)  # Descending Order
print(list)

list.reverse()
print(list)

list.insert(1,43)
print(list)

list.remove(43)
print(list)

list.pop(1)
print(list)

# print the index
index = list.index(32)
print(index)