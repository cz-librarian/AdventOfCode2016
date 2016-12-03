from copy import deepcopy
import numpy

puzzle_fp = open("01")
# Get rid of whitespaces in instructions
puzzle_input = [char.rstrip().lstrip() for char in puzzle_fp.read().split(",")]
puzzle_fp.close()

facing = ["N", "E", "S", "W"]
top = facing[0]
# x,y
coordinates = [0, 0]
X = 0
Y = 1
visited_coordinates = []
found= False

def first_part():
    global top
    for instruction in puzzle_input:
        distance = int(instruction[1:])
        if "R" in instruction:
            if top == "N":
                top = "E"
                for step in range(distance):
                    coordinates[X] += 1
            elif top == "E":
                top = "S"
                coordinates[Y] -= distance
            elif top == "S":
                top = "W"
                coordinates[X] -= distance
            elif top == "W":
                top = "N"
                coordinates[Y] += distance

        elif "L" in instruction:
            if top == "N":
                top = "W"
                coordinates[X] -= distance
            elif top == "E":
                top = "N"
                coordinates[Y] += distance
            elif top == "S":
                top = "E"
                coordinates[X] += distance
            elif top == "W":
                top = "S"
                coordinates[Y] -= distance

    print coordinates
    print abs(coordinates[X]) + abs(coordinates[Y])


def second_part():
    global top
    x_size = 250
    y_size = 250
    visited = numpy.zeros((x_size, y_size)).tolist()

    for instruction in puzzle_input:
        distance = int(instruction[1:])
        if "R" in instruction:
            if top == "N":
                top = "E"
                for step in range(distance):
                    coordinates[X] += 1
                    move(visited, coordinates)

            elif top == "E":
                top = "S"
                for step in range(distance):
                    coordinates[Y] -= 1
                    move(visited, coordinates)

            elif top == "S":
                top = "W"
                for step in range(distance):
                    coordinates[X] -= 1
                    move(visited, coordinates)

            elif top == "W":
                top = "N"
                for step in range(distance):
                    coordinates[Y] += 1
                    move(visited, coordinates)

        elif "L" in instruction:
            if top == "N":
                top = "W"
                for step in range(distance):
                    coordinates[X] -= 1
                    move(visited, coordinates)

            elif top == "E":
                top = "N"
                for step in range(distance):
                    coordinates[Y] += 1
                    move(visited, coordinates)

            elif top == "S":
                top = "E"
                for step in range(distance):
                    coordinates[X] += 1
                    move(visited, coordinates)

            elif top == "W":
                top = "S"
                for step in range(distance):
                    coordinates[Y] -= 1
                    move(visited, coordinates)


def move(visited_coords, coords):
    global found
    if visited_coords[coords[X]][coords[Y]] == 0:
        visited_coords[coords[X]][coords[Y]] = 1
    elif not found:
        print abs(coords[X]) + abs(coords[Y])
        found = True

first_part()
# second_part()
