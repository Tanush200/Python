students = set()
print(type(students))


students.add(1)
students.add(2)
# students.remove(2)
# students.clear() 
students.pop()
print(students)

# Sets --> mutable 
# Elements in Sets --> immutable


set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
