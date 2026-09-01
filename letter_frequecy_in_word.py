word = input("enter the word-")
count = {}
for i in range(len(word)):
    if word[i] not in count:
        count[word[i]] = 1
    elif word[i] in count:
        count[word[i]] += 1
print(count)


