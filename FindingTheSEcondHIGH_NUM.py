largest = 0
second = 0
i = 0
num = int(input("enter-"))
while i < num:
    rem = num % 10
    if largest < rem:
        second = largest
        largest = rem
    elif second < rem :
        second = rem 
    num = num // 10
    i +=1
print(largest)
print(second)
