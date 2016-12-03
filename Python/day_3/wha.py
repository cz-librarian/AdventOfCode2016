import sys

print range(0,len("fdffdfdf"),3)

puzzle_fp = open("03")
puzzle_input = puzzle_fp.readlines()
puzzle_fp.close()

def is_triangle(tri):
    print tri[0%3],tri[(1+1)%3],tri[(2+2)%3],
    print all([tri[i%3] + tri[(i+1)%3] > tri[(i+2)%3] for i in range(3)])
    return all([tri[i%3] + tri[(i+1)%3] > tri[(i+2)%3] for i in range(3)])

in_str = [line.strip() for line in puzzle_input]
in_list = [[int(side) for side in line.split()] for line in in_str]

#y print("part 1: ", len(list(filter(is_triangle, in_list))))
import os
os.system("cls")
triangles = []
in_list.reverse()
while in_list:
    square = [in_list.pop() for _ in range(3)]
    for triangle in [[square[y][x] for y in range(3)] for x in range(3)]:
        triangles.append(triangle)

# print("part 2: ", len(list(filter(is_triangle, triangles))))