rows=5
for i in range(rows):
    for j in range(i+1):
        print(chr(65+rows+j-i-1),end="")
    print()
