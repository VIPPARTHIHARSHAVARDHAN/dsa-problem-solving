n = 4
size = 2 * n - 1

for i in range(size):
    for j in range(size):

        top = i
        left = j
        bottom = size - 1 - i
        right = size - 1 - j

        minimum = min(top, left, bottom, right)

        print(n - minimum, end=" ")

    print()