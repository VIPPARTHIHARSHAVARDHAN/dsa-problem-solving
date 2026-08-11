rows=5
for i in range(rows,0,-1):
    for j in range(i-1):
        print( " ", end="")
    for j in range(2*(rows-i)+1):
        print( "*", end="")
    print()