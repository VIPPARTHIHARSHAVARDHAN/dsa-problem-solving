rows=4
for i in range(rows):
    if i==0 or i==rows-1 :
        for j in range(rows):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(rows-2):
            print(" ",end="")
        print("*",end="")
    print()