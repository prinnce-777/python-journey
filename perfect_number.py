num = (input("enter-"))
count = 0
for i in range(1,int(num) + 1):
    if int(num) % i ==0 and i < int(num):
        count = count + i
print(count)
if count == int(num):
    print("it is perfect number")
else:
    print("it is not perfect number")