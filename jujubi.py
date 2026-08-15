num = input("enter-")
largest = 0
second = 0
for i in range(0,len(num)):
    if largest < int(num[i]):
        second = largest
        largest =  int(num[i])
    elif second <  int(num[i]):
        second =  int(num[i])
print(f"highest number = {largest}")
print(f"second highest = {second}")