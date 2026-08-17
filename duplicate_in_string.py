word = input("enter the word-")
letter = input("enter the letter-")
count = 0
for i in range (0,len(word)):
    if letter in word[i]:
      count += 1
print(f"letter {letter} is printing {count} times in word {word}")
if count >= 2:
   print(f"this letter '{letter}' is duplicate")
