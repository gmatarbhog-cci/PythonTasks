import math


def calculate_robot_movements(movements):
    initial_position = (0, 0)
    up, down = 0, 0
    left, right = 0, 0
    print("My initial position is {}".format(initial_position))
    for movement in movements:
        direction = movement
        step = movements[movement]
        match direction:
            case "U":
                up += step
                print('Moving up {} steps'.format(step))
            case "D":
                down += step
                print('Moving down {} steps'.format(step))
            case "L":
                left += step
                print('Moving left {} steps'.format(step))
            case "R":
                right += step
                print('Moving right {} steps'.format(step))

    pos_x = right - left
    pos_y = up - down
    current_position = (pos_x, pos_y)
    print("My current position is {}".format(current_position))
    distance = math.sqrt(((initial_position[0] - current_position[0]) ** 2) + ((initial_position[1] - current_position[1]) ** 2))
    print("My distance from start point to current point is {}".format(int(distance)))


calculate_robot_movements({"U": 5, "D": 3, "L": 3, "R": 2})
