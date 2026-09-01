sentence = input("enter the sentence-")
words=(sentence.split())
print(words)
count = {}
for i in range (len(words)):
    if words[i]not in count:
        count[words[i]] = 1
    elif words[i] in count:
        count[words[i]] += 1
print(count)
