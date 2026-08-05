def addition(a):
    sum = 1
    for x in range(1,a+1):
        sum = sum * x
    print(f"the factorial of {a} is = {sum}")
a = int(input("enter-"))
addition(a)
