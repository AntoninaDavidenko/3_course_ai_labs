def and_func(param1, param2):
    s = param1 * w + param2 * w
    if s < 1.5:
        fs = 0
    else:
        fs = 1
    return fs


w = 1
print("AND")
print("x1: 0, x2: 0   result:", and_func(0, 0))
print("x1: 1, x2: 0   result:", and_func(1, 0))
print("x1: 0, x2: 1   result:", and_func(0, 1))
print("x1: 1, x2: 1   result:", and_func(1, 1))
