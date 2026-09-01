name = input("enter-")
enter =input("enter-")
count = 0
for i in range(0,len(name)):
    if enter == name[i]:
        count += 1
print(f"the number of times '{enter}' letter in word '{name}' = {count}")