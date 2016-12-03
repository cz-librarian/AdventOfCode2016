from argparse import _AppendAction
from gettext import c2py

puzzle_fp = open("03")
puzzle_input = puzzle_fp.readlines()
puzzle_fp.close()


# 1649
def triangulate(x, y, z):
    a = x + y > z
    b = y + z > x
    c = x + z > y
    # print x, y, z, a and b and c
    return a and b and c


def part_one(fname):
    puzzle_fp = open(fname)
    puzzle_input = puzzle_fp.readlines()
    puzzle_fp.close()
    count = 0

    for line in puzzle_input:
        a, b, c = [int(el) for el in line.lstrip().rstrip().split(" ") if el != ""]
        if triangulate(a, b, c) and triangulate(b, c, a) and triangulate(c, a, b):
            count += 1
    print count


def part_two():
    count = 0
    a_column = []
    b_column = []
    c_column = []
    for line in puzzle_input:
        a, b, c = [int(el) for el in line.lstrip().rstrip().split(" ") if el != ""]
        a_column.append(a)
        print c
        b_column.append(b)
        c_column.append(c)

    tri = []
    # print len(a_column)
    # print len(b_column)
    # print len(c_column)

    # print a_column
    for a in a_column:
        if len(tri) == 3:
            if triangulate(*tri):
                count += 1
            # print count
            tri = []
        else:
            tri.append(a)
    # print b_column
    for b in b_column:
        if len(tri) == 3:
            if triangulate(*tri):
                count += 1
            tri = []
        else:
            tri.append(b)
    # print c_column
    for c in c_column:
        if len(tri) == 3:
            if triangulate(*tri):
                count += 1
            tri = []
        else:
            tri.append(c)

    # print count
    tri = []
    for i,el in enumerate(a_column):
        if len(tri) == 3:
            if triangulate(*tri):
                count += 1
            # print count
            tri = []
        else:
            tri.append(a)

    """
    size = len(one_list_input) // 3
    print one_list_input[::3]
    print one_list_input[1::3]
    print one_list_input[2::3]
    print size
    for i, el in enumerate(one_list_input[::3]):
        if i < size:
            if triangulate(el, el + 1, el + 2):
                count += 1

    for i, el in enumerate(one_list_input[1::3]):
        if i < size:
            if triangulate(el, el + 1, el + 2):
                count += 1

    for i, el in enumerate(one_list_input[2::3]):
        if i < size:
            if triangulate(el, el + 1, el + 2):
                count += 1
    print count"""





def damn():
    count = 0
    a_column = []
    b_column = []
    c_column = []
    for line in puzzle_input:
        a, b, c = [int(el) for el in line.lstrip().rstrip().split(" ") if el != ""]
        a_column.append(a)
        b_column.append(b)
        c_column.append(c)

    f_a = open("a","w")
    for tria in range(0, len(a_column), 3):
        f_a.write(str(a_column[tria]) + " " + str(a_column[tria + 1]) + " " + str(a_column[tria]) + "\n")
    f_a.close()

    f_b = open("b","w")
    for tria in range(0, len(b_column), 3):
        f_b.write(str(b_column[tria]) + " " + str(b_column[tria + 1]) + " " + str(b_column[tria]) + "\n")
    f_b.close()

    f_c = open("c","w")
    for tria in range(0, len(c_column), 3):
        f_c.write(str(c_column[tria]) + " " + str(c_column[tria + 1]) + " " + str(c_column[tria]) + "\n")
    f_c.close()
part_one("a")
part_one("b")
part_one("c")