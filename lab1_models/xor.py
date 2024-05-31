import numpy as np

def xor_func(param1, weight1, weight2):
    s = np.dot(param1, weight1)
    sh = []
    sf = []
    for i in s:
        if i < 0.5:
            sh.append(0)
        else:
            sh.append(1)
    sh = np.array(sh)
    so = np.dot(sh, weight2)
    for j in so:
        if j < 0.5:
            sf.append(0)
        else:
            sf.append(1)
    sf = np.array(sf)
    return sf[0]


x1 = np.array([0, 0])
x2 = np.array([0, 1])
x3 = np.array([1, 0])
x4 = np.array([1, 1])

w1 = np.array([[1, -1],
              [-1, 1]])
w2 = np.array([[1], [1]])

print("XOR")
print("x1: 0, x2: 0   result:",  xor_func(x1, w1, w2))
print("x1: 0, x2: 1   result:", xor_func(x2, w1, w2))
print("x1: 1, x2: 0   result:", xor_func(x3, w1, w2))
print("x1: 1, x2: 1   result:", xor_func(x4, w1, w2))
