name = "Other Name"
if(name == "Saha"):
    print("True")
elif(name == "Tanush"):
    print("Matched")
else:
    print("Not Matched")


# Nesting 
age = 15
if(age >= 18):
    if(age >= 80):
        print("Cannot Drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")


# Even and Odd :
num = float(input("Enter the number : "))
if(num % 2 == 0):
    print("Number is even")
else:
    print("number is odd")


# Max of three numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

result = max(num1,num2,num3)
print("The Max number is : ",result)
