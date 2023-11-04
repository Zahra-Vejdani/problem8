n=int(input("enter n please: "))
m=int(input("enter m please: "))

for i in range (n):
    for j in range (m):
        if (i+j)% 2 ==0:
            print("*", end="")
        else:
            print("#", end="")
    print()

    