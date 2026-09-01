list = [1,2,3,4,4,5,6]
count = {}
for i in range(0,len(list)):
    if list[i] not in count:
        count[list[i]] = 1
    elif list[i] in count:
        count[list[i]] += 1
freq = count

##print(freq[list[3]])  #this indicates the frequency of the element at index 3 in the list, which is 4. The output will be 2

max = freq[list[0]]
for k in range(1,len(list)):
    if freq[list[k]] > max:
        max = freq[list[k]]
        count1 = ""
        count1 = list[k]
print(f"The max frequency is: {max}, and the element is: {count1}")