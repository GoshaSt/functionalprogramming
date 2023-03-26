def composite_functions(f, g):
    def h(x, y):
        return f(g(x, y))

    return h


def f(x):
    return x * x


def g(x, y):
    return x + y


h = composite_functions(f, g)
result = h(4, 9)
print("Result: {result}")
