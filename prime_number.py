num = int(input("enter-"))
count = 0
for i in range(1,num + 1):
    if num % i==0:
        print(i)
        count += 1
if count == 2:
    print("it is prime number")
else:
    print("it is not prime number")
        