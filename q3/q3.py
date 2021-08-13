def pascal_triangle(n):
    result = []
    for row in range(n):
        col = 0
        cols = []
        while (col<=row):
            if col == 0 or col == row:
                cols.append(1)
            else:
                cols.append(result[row - 1][col - 1] + result[row - 1][col])
            col += 1
        result.append(cols)
    return result

print(pascal_triangle(4))