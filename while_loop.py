num = int(input("enter the number-"))
count = 0
while num > 1:
    count +=1
    if num % 2 == 0:
       num = num/2
    else:
         num = num -1
print(f"count is {count}")
  