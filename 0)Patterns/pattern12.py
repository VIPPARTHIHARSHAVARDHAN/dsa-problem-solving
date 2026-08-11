rows=5
for i in range(rows-1):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(rows+1-(2*i)):
        print(" ",end="")
    for j in range(i+1):
        print(i-j+1,end="")
    print()
    