table = [x for x in range(0,22,2)]
print(table)

#squares = [x**2 for x in range(9) if x % 2 == 0]
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)