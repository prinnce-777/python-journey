name = input("enter-")
name = (name.split(" "))
max = len(name[0])
big = ""
for i in range(1,len(name)):
    if max < len(name[i]):
        max2 = max
        max = len(name[i])
    elif max2 < len(name[i]):
        max2 = len(name[i])
print(f"the longest word has {max} letters")
print(f"the second longest word has {max2} letters")
for j in range(0,len(name)):
    if max == len(name[j]):
        print(f"the longest word is {name[j]}")
        break


