name = input("enter-")
oname = name
fname =""
for i in range(len(name)-1,-1,-1):
    fname = fname + name[i]
if oname == fname:
    print("yees it is pand")
else:
    print("no it is not pand")