a = "  hallo herr.mahesh how are you " #gave two spaces at intial and one space at ending
print(a[13])
for x in a:
    print(x + x, end="")
print(len(a))
if 'ha' in a:
    print("yes")
if 'ab' not in a:
    print("no")
print(a.upper())
print(a.lower())
print(a.strip())            #gave gap at intial and at ending but strip function  will remove that gap
print(a.replace("ha","ja")) 
print(a.split(" "))
print(a[2:5])
print(a[5:])
print(a[:3])