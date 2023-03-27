combinacoes = [
    (True, True),
    (True, False),
    (False, True),
    (False, False),
]
for x, y in combinacoes:
    print(f"{x} or {y} -> {x or y}")
