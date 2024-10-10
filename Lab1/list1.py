# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:22:55 2024

@author: Student
"""
import matplotlib.pyplot as plt
import random

# Task 1


def weekday(day: int, month: int, year: int) -> str:
    """ """
    week_days = {0: "Sunday", 1: "Monday", 2: "Tuesday",
                 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    y0 = year - (14 - month) // 12
    x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (day + x + (31 * m0) // 12) % 7

    return week_days[d0]
# Task 2


def segment_length(Ap: float, Ak: float, Bp: float, Bk: float):
    """ """
    start_A = min(Ap, Ak)
    end_A = max(Ap, Ak)
    start_B = min(Bp, Bk)
    end_B = max(Bp, Bk)
    start_intersection = max(start_A, start_B)
    end_intersection = min(end_A, end_B)

    if end_intersection <= start_intersection:
        return None
    else:
        return (start_intersection, end_intersection)
# Task 3


def random_walk(number_of_steps: int):
    """ """
    start_point = (0, 0)
    movement = []
    movement.append(start_point)
    if number_of_steps == 0:
        return movement

    for i in range(1, number_of_steps+1):
        range_x_min = movement[len(movement) - i][0] - 1
        range_x_max = movement[len(movement) - i][0] + 1

        range_y_min = movement[len(movement) - i][1] - 1
        range_y_max = movement[len(movement) - i][1] + 1

        x_coordinate = random.choice([range_x_min, range_x_max])
        y_coordinate = random.choice([range_y_min, range_y_max])
        coordinates = (x_coordinate, y_coordinate)
        movement.append(coordinates)
    return movement


# print(weekday(10, 10, 2024))
# print(segment_length(2, 7, 5, 9))
print(random_walk(10))
