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
    s1 = np.dot(current_set, w1)
    h_node1 = sigmoid(s1)

    sh1 = np.dot(h_node1, w2)
    h2_node1 = sigmoid(sh1)

    sf1 = np.dot(h2_node1, w3)
    f_node1 = sigmoid(sf1)
    return f_node1[0][0], f_node1[0][1]


learning_rate = 0.1
epochs = 1000

input_nodes = 36
hidden_nodes = 20
hidden_nodes2 = 10
output_nodes = 2

w1 = np.random.randn(input_nodes, hidden_nodes)
w2 = np.random.randn(hidden_nodes, hidden_nodes2)
w3 = np.random.randn(hidden_nodes2, output_nodes)


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
        h2_node = sigmoid(sh)

        sf = np.dot(h2_node, w3)
        f_node = sigmoid(sf)

        ef = correct_answer - f_node
        ef_delta = ef * sigmoid_derivative(f_node)
        eh2 = np.dot(ef_delta, w3.T)
        eh2_delta = eh2 * sigmoid_derivative(h2_node)
        eh = np.dot(eh2_delta, w2.T)
        eh_delta = eh * sigmoid_derivative(h_node)

        w3 += np.dot(h2_node.T, ef_delta) * learning_rate
        w2 += np.dot(h_node.T, eh2_delta) * learning_rate
        w1 += np.dot(current_set.T, eh_delta) * learning_rate

test_file_name = 'test1.test'
test_data, test_answer = read(test_file_name)
for data in test_data:
    number_one, number_two = test(data)
    print(f"Predicted Output: {number_one} {number_two}")

