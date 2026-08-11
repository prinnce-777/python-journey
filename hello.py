num = [22,23,24,24,25]
print(len(num))
max = num[0]
for i in range(1,len(num)):
    if max < num[i]:
        max = num[i]
print(max)

