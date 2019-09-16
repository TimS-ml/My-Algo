directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

i, j = 1, 1

for direct in directions:
    new_i = i + direct[0]
    new_j = j + direct[1]
    print(new_i, new_j)
