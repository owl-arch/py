# Teste de performance CPynthon Vs PyPy
result = []
for a in range(10000):
    for b in range(10000):
        if (a+b) % 11 == 0:
            result.append((a, b))
