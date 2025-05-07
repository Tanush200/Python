def sum(a,b):
  return a+b
sum(2,34)


list = input("Enter the list name: ")
def length_list(list):
  return len(list)
print(length_list(list))


heros = ["Tanush","Saha","10000223006","231000110630"]
def print_line(list):
  for ele in list:
    print(ele , end=" ") # single line keyword end = " " , nextline command end = "\n"
print_line(heros)



def converter(value):
  inr_value = value * 84.75
  return inr_value
converter(66)