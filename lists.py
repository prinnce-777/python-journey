num = [1,2,4,3,0,67,78,66,921]
i =0
min = num[0]
while i < len(num):
    if min > num[i]:
        min = num[i]
    i += 1
print(min)