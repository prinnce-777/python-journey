num =(input("enter-"))
count = 0
for i in range(0,len(num)):
  count1 = int(int(num[i]) ** len(num))
  count = count + count1
print(count)
if count == int(num):
  print("it is armstrong number")
else:
 print("it is  not armstrong number")

