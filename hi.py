name = input("enter-")
vowels =["a","e","i","o","u"]
count = 0
for i in range(len(name)):
    if name[i] in vowels:
        count += 1
print(f"there are {count} vowels in  word {name}")
