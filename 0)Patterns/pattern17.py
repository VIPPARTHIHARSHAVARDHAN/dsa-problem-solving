rows=5
for i in range(rows,1,-1):
    for j in range(i-2):
        print(" ",end="")
    for j in range(rows-i+1):
        print(chr(65+j),end="")
    for j in range(rows-i-1,-1,-1):
        print(chr(65+j),end="")
   
    print()
