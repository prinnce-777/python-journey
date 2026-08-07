num = [1,2,4,3,0,67,78,66,921]
i =0
min = num[0]
while i < len(num):
    if min > num[i]:
        min = num[i]
    i += 1
print(min)
num.sort()   #it will sort the list in ascending order
print(num)

list = ["abhi", 34, 3.14, "hello", 3.14]
print(list)
if "hello" in list:
    print("yes")
list[0] = "prinnce"
list.append("python")
list.insert(0, 7770)
list.remove(3.14)    #if there is more than one 3.14 then it will remove the first one
list.pop(0)          #removes first element
#list.clear()        #it clears the whole list
list.reverse()
print(list)

the_list = num.copy()
print(the_list)