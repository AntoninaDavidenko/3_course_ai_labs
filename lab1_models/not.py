def not_func(param):
    s = param * w
    if s < -1:
        fs = 0
    else:
        fs = 1
    return fs


w = -1.5
print("NOT")
print("x: 0  result:",  not_func(0))
print("x: 1  result:", not_func(1))
