def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Invalid input"

print(add(5, 3))
