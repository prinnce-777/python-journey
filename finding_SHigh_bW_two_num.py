largest = 0
second = 0
for i in range(2):
    num =int(input("enter="))
    if largest < num:
        second = largest
        largest = num
    elif second < num:
        second = num
print(second)
