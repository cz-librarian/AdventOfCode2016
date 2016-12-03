"""
--- Day 2: Bathroom Security ---
1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?



    x=  0 1 2
y =  0  1 2 3
     1  4 5 6
     2  7 8 9

y ~= (0,1,2)
x ~= (0,1,2)


You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy
 conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay,
 the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of
  bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

    c=  0 1 2 3 4
r =  0      1                   0,2
     1    2 3 4           1,1   1,2  1,3
     2  5 6 7 8 9   2,0   2,1   2,2  2,3   2,4
     3    A B C           3,1   3,2  3,3
     4      D                   4,2
y ~= (0,1,2)
x ~= (0,1,2)

You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very
different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

"""
import numpy
import sys


def part_one():
    # Init phase
    columns = 3
    rows = 3
    keypad = numpy.zeros((columns, rows)).tolist()
    # You start at "5"
    curr_x = 1
    curr_y = 1

    for r in xrange(rows):
        for c in xrange(columns):
            keypad[c][r] = (c + 1) + r * columns
    # -------------------------------------------


    # Input
    puzzle_fp = open("02")
    puzzle_input = puzzle_fp.readlines()
    puzzle_fp.close()

    # ------------------------------------------


    def up(y):
        if y != 0:
            return y - 1
        else:
            return y

    def down(y):
        if (y + 1) != rows:
            return y + 1
        else:
            return y

    def left(x):
        if x != 0:
            return x - 1
        else:
            return x

    def right(x):
        if (x + 1) != columns:
            return x + 1
        else:
            return x

    for line in puzzle_input:
        for char in line:
            # U moves up, D moves down, L moves left, and R moves right
            if char == "U":
                curr_y = up(curr_y)
            elif char == "D":
                curr_y = down(curr_y)
            elif char == "L":
                curr_x = left(curr_x)
            elif char == "R":
                curr_x = right(curr_x)

        print keypad[curr_x][curr_y]


def part_two():
    # Init phase
    columns = 5
    rows = 5
    keypad = numpy.zeros((columns, rows)).tolist()
    # You start at "5"
    curr_x = 0
    curr_y = 2

    bathroom_keypad_buttons = [str(pad) for pad in xrange(1, 10)] + ["A", "B", "C", "D"]
    bathroom_keypad_pads = [(0, 2)]
    bathroom_keypad_pads += [(1, y) for y in xrange(1, 4)]
    bathroom_keypad_pads += [(2, y) for y in xrange(5)]
    bathroom_keypad_pads += [(3, y) for y in xrange(1, 4)]
    bathroom_keypad_pads += [(4, 2)]

    for button, pad in enumerate(bathroom_keypad_pads):
        keypad[pad[0]][pad[1]] = bathroom_keypad_buttons[button]

    # -------------------------------------------

    # Input
    puzzle_fp = open("02")
    puzzle_input = puzzle_fp.readlines()
    puzzle_fp.close()

    # ------------------------------------------

    def up(x, y):
        if y != 0:
            if keypad[x][y - 1] != 0:
                return y - 1
        return y

    def down(x, y):
        if (y + 1) != rows:
            if keypad[x][y + 1] != 0:
                return y + 1
        return y

    def left(x, y):
        if x != 0:
            if keypad[x - 1][y] != 0:
                return x - 1
        return x

    def right(x, y):
        if (x + 1) != columns:
            if keypad[x + 1][y] != 0:
                return x + 1
        return x

    for i in range(5):
        for j in range(5):
            print (i,j),
            print keypad[i][j],
        print
    for line in puzzle_input:
        for char in line:
            # U moves up, D moves down, L moves left, and R moves right
            if char == "U":
                curr_y = up(curr_x, curr_y)
            elif char == "D":
                curr_y = down(curr_x, curr_y)
            elif char == "L":
                curr_x = left(curr_x, curr_y)
            elif char == "R":
                curr_x = right(curr_x, curr_y)

        print keypad[curr_y][curr_x]


part_two()
