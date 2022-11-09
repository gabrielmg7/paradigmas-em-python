valores = [1, 2, 3, 4, 5, 6]

funcaox = lambda x: filter(lambda item: item % 2 == 0, x) * 3

print(funcaox(valores))