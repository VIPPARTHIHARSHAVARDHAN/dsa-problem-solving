rows=5

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    
    for j in range((rows-i-1)*2):
        print(" " , end="")
    
    
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows-1,0,-1):
    for j in range(i):
        print("*",end="")
    
    for j in range((rows-i)*2):
        print(" " , end="")
    
    
    for j in range(i):
        print("*",end="")
    print()