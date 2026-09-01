name =input("e-")
count = 0
letter =input("enter your letter")
for i in range(0,len(name)):
    if letter in name[i]:
        count += 1
print(f"{count} times the letter {letter} found in word {name}")
