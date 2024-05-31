import numpy as np


def read(file_name):
    with open(file_name, 'r') as file:
        file = file.readlines()
    # Отримання інформації з першого рядка
    counts = list(map(int, file[0].split()))
    count_images = counts[0]
    image_length = counts[1]
    answer_length = counts[2]

    # Обробка всіх інших рядків
    data = []
    for line in file[1:]:
        line = line.strip().replace(" ", "")
        data.append(line)

    # Перетворення списку на один рядок
    data = "".join(data)

    dataset_ = []
    answer_set_ = []
    i = 0
    while i < len(data):
        tempdata = []
        temp_answer = []
        for _ in range(image_length):
            # Перевірка, щоб уникнути виходу за межі списку data
            if i < len(data):
                tempdata.append(int(data[i]))
                i += 1
        dataset_.append(tempdata)

        for _ in range(answer_length):
            # Перевірка, щоб уникнути виходу за межі списку data
            if i < len(data):
                temp_answer.append(int(data[i]))
                i += 1
        answer_set_.append(temp_answer)

    dataset_ = np.array(dataset_)
    answer_set_ = np.array(answer_set_)

    return dataset_, answer_set_


def test(test_dataset):
    s1 = np.dot(test_dataset, w1)
    h_node1 = sigmoid(s1)

    sh1 = np.dot(h_node1, w2)
    f_node1 = sigmoid(sh1)
    return f_node1[0], f_node1[1]


learning_rate = 0.1
epochs = 1000

input_nodes = 36
hidden_nodes = 36
output_nodes = 2

w1 = np.random.randn(input_nodes, hidden_nodes)
w2 = np.random.randn(hidden_nodes, output_nodes)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


train_file_name = 'test1.train'
dataset, answer_set = read(train_file_name)


for epoch in range(epochs):
    for j in range(len(dataset)):
        current_set = np.array(dataset[j], ndmin=2)
        correct_answer = np.array(answer_set[j], ndmin=2)
        s = np.dot(current_set, w1)
        h_node = sigmoid(s)

        sh = np.dot(h_node, w2)
        f_node = sigmoid(sh)

        ef = correct_answer - f_node
        ef_delta = ef * sigmoid_derivative(f_node)
        eh = np.dot(ef_delta, w2.T)
        eh_delta = eh * sigmoid_derivative(h_node)

        w2 += np.dot(h_node.T, ef_delta) * learning_rate
        w1 += np.dot(current_set.T, eh_delta) * learning_rate

test_file_name = 'test1.test'
test_data, test_answer = read(test_file_name)
for data in test_data:
    number_one, number_two = test(data)
    print(f"Predicted Output: {number_one} {number_two}")