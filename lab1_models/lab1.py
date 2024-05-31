import numpy as np


# x1    x2    x3    x4    x5    x6    x7    x8    x9    x10   x11   x12   x13   x14   x15
# 2.56, 4.20, 1.60, 4.29, 1.17, 4.40, 0.88, 4.14, 0.07, 4.77, 1.95, 4.18, 0.04, 5.05, 1.40
dataset = np.array([[2.56, 4.20, 1.60],
                    [4.20, 1.60, 4.29],
                    [1.60, 4.29, 1.17],
                    [4.29, 1.17, 4.40],
                    [1.17, 4.40, 0.88],
                    [4.40, 0.88, 4.14],
                    [0.88, 4.14, 0.07],
                    [4.14, 0.07, 4.77],
                    [0.07, 4.77, 1.95],
                    [4.77, 1.95, 4.18]])

answer_set = [4.29, 1.17, 4.40, 0.88, 4.14, 0.07, 4.77, 1.95, 4.18, 0.04]

input_nodes = 3
output_nodes = 1

learning_rate = 0.01
max_epoch = 10000

w = np.random.rand(input_nodes, output_nodes)

e0 = 0

for epoch in range(0, max_epoch):
    total_e = 0
    for i in range(len(dataset)):
        current_set = np.array(dataset[i])
        correct_answer = answer_set[i]
        s = np.dot(current_set, w)
        y = 1 / (1 + np.exp(-s)) * 10
        error = (y - correct_answer) ** 2
        total_e += error

    if abs(total_e - e0) < 0.001:
        max_epoch = epoch
        # for i in range(len(dataset)):
        #     current_set = np.array(dataset[i])
        #     correct_answer = answer_set[i]
        #     s = np.dot(current_set, w)
        #     y = 1 / (1 + np.exp(-s)) * 10
        #     error = (y - correct_answer) ** 2
        #     total_e += error
        #     print("Train")
        #     print("Predicted:", y[0], "actual:", answer_set[i], "error:", y[0] - correct_answer)
        break

    e0 = total_e
    for i in range(len(dataset)):
        current_set = np.array(dataset[i])
        correct_answer = answer_set[i]
        s = np.dot(current_set, w)
        y = 1 / (1 + np.exp(-s)) * 10

        error_derivative = (y - correct_answer) * (np.exp(-s) / (1 + np.exp(-s)) ** 2)
        w_delta = (-learning_rate) * error_derivative * current_set
        for j in range(len(w)):
            w[j] += w_delta[j]


def test(test_dataset):
    s1 = np.dot(test_dataset, w)
    y1 = 1 / (1 + np.exp(-s1)) * 10
    return y1[0]


test_data1 = np.array([1.95, 4.18, 0.04])
test_data2 = np.array([4.18, 0.04, 5.05])

test_answer1 = 5.05
test_answer2 = 1.40

print("epochs used for training:", max_epoch)

print("Test")
print("predicted:", test(test_data1), "actual:", test_answer1, "error:", test_answer1 - test(test_data1))
print("predicted:", test(test_data2), "actual:", test_answer2, "error:", test_answer2 - test(test_data2))





