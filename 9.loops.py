# Simple While loop
count = 1
while count <=5:
  print("Tanush")
  count +=1


# Print array using while loop
nums = [1,243,4,5,66,34534,3425235324,5]
i = 0
n = len(nums)
while i < n:
  print(nums[i])
  i +=1

# break & continue
i = 1
while i <= 5:
  if(i == 3):
    i += 1
    continue
  print(i)
  i+=1
print("Loop Ended")


# For Loop -1
nums = [1,2,3,5]
for num in nums:
  print(num)


# For Loop -2
for num in nums:
  if(num == 3):
    print("3 Found")
    break
  else:
    print(num)
else:
  print("Loop Ended")

# range method in for loop 
for i in range(5): # range(stop) 
  print(i)

for i in range(2,8):  # range(start?,stop) 
  print(i)

for i in range(2,11,2): #  # range(start?,stop,step?)
  print(i) 


for i in range(1,100):
  pass
print("Passed")


# WAP to find the sum of all numbers in range 
n = 5
sum = 0
i = 1

while i <=n : 
  sum += i
  i+=1
print(sum)


