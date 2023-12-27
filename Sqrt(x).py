x = 8
squares_1_to_5 = [1, 1, 1, 2, 2]
if x in range(1, 6):
    print(squares_1_to_5[x-1])

squares = [i**2 for i in range(x//2)]
print(squares)
print(x**0.5)