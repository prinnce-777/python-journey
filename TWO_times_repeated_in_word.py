word = input("enter=")
count = 0
empty = ""
for i in range(0,len(word) -  1):
    if word[i].lower == word[i + 1].lower:
     empty = empty + word[i]
     break
print(f"the first letter to appered twice in word '{word}' is '{empty}'" )


