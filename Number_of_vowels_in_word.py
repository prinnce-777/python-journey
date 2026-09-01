name = input("enter")
vowels =["a","e","i","o","u"]
count = 0
count1 = 0
for i in range(0,len(name)):
    if name[i] in vowels:
        print(name[i])
        count += 1
    else:
        count1 += 1
print(f"the number of vowels in word ={count}")
print(f"the number of consonants in word ={count1}")
    