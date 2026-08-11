rows=5
for i in range(1,rows):
    for j in range(i):
        print( "*", end="")
    print()
for i in range(rows,0,-1):
    for j in range(i):
        print( "*", end="")
    print()