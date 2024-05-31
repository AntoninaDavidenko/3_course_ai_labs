import numpy as np

R = [[-1, 0, -1, -1, -1, -1, -1, -1, -1],
     [0, -1,  0, -1, -1, -1,  0, -1, -1],
     [-1, 0, -1,  0, -1, -1, -1, -1, -1],
     [-1, -1, 0, -1,  0, -1, -1, -1, -1],
     [-1, -1, -1, 0, -1,  0, -1,  0, 100],
     [-1, -1, -1, -1, 0, -1,  0,  0, -1],
     [-1,  0, -1, -1, -1, 0, -1, -1, -1],
     [-1, -1, -1, -1,  0, 0, -1, -1, 100],
     [-1, -1, -1, -1, 0, -1, -1,  0, 100]]

gamma = 0.8
Q = [[0 for j in range(9)] for i in range(9)]

for i in range(500):
    # текущая комната
    first_room = 5 #np.random.randint(0, 8)
    room = first_room
    done = False
    while not done:

        # выбираем куда идти
        row = R[room]
        available_rooms = []
        next_room = None
        # если есть комната с 100, то это следующая комната
        for x in range(len(row)):
            if row[x] == 100:
                next_room = x
        #
        if next_room is None:
            for x in range(len(row)):
                if row[x] >= 0:
                    available_rooms.append(x)
            next_room = np.random.choice(available_rooms)

        Q[room][next_room] = R[room][next_room] + gamma * np.max(Q[next_room])

        if R[room][next_room] == R[8][8]:
            done = True

        room = next_room


cat_position = 0
cat_finish = 8
way_through_rooms = [cat_position]
while True:
    next_position = np.argmax(Q[cat_position])
    cat_position = next_position
    way_through_rooms.append(next_position)
    if cat_position == cat_finish:
        break

print(way_through_rooms)
for row in Q:
    print(row)
