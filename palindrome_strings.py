a = input("e-")
pali = 0
for i in range(len(a) - 1,-1,-1):
    rem = int(int(a[i]) % 10)
    pali = pali * 10 + rem
if int(a) == (pali):
    print("it is pali")
else:
    print("it is not pali")
