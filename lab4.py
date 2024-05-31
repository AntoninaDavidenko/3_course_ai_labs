import numpy as np

R = [[-1, 0, -1, -1, -1, -1, -1, -1, -1],
     [0, -1,  0, -1, -1, -1,  0, -1, -1],
     [-1, 0, -1,  0, -1, -1, -1, -1, -1],
     [-1, -1, 0, -1,  0, 0, -1, -1, -1],
     [-1, -1, -1, 0, -1,  0, -1,  0, 100],
     [-1, -1, -1, 0, 0, -1,  0,  0, -1],
     [-1,  0, -1, -1, -1, 0, -1, -1, -1],
     [-1, -1, -1, -1,  0, 0, -1, -1, 100],
     [-1, -1, -1, -1, 0, -1, -1,  0, 100]]

gamma = 0.8
Q = [[0 for j in range(9)] for i in range(9)]

for i in range(400):
    # Поточна кімната
    first_room = np.random.randint(0, 8)
    room = first_room
    done = False
    previous_step_room = None
    while not done:
        row = R[room]
        available_rooms = []
        next_room = None
        # Якщо є кімната зі 100, то це наступна кімната
        for x in range(len(row)):
            if row[x] == 100:
                next_room = x

        if next_room is None:
            for x in range(len(row)):
                if row[x] >= 0:
                    available_rooms.append(x)
            next_room = np.random.choice(available_rooms)

        if previous_step_room is not None:
            hhh = np.max(Q[room])
            Q[previous_step_room][room] = R[previous_step_room][room] + gamma * np.max(Q[room])

            if previous_step_room == 8 and room == 8:
                done = True
        previous_step_room = room
        room = next_room


def get_way(cat_position, cat_finish):
    way_through_rooms = [cat_position]
    while True:
        next_position = np.argmax(Q[cat_position])
        cat_position = next_position
        way_through_rooms.append(next_position)
        if cat_position == cat_finish:
            break
    return way_through_rooms


way = get_way(0, 8)
print("The shortest way:", *way)
print("Q matrix")
for row in Q:
    print(*row)

