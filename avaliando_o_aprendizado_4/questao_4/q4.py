valores = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

funcaox = lambda x: filter(lambda item: item % 2 == 0, x) * 3.0

print(funcaox(valores))