# Exercise
# ● Create Point namedtuple
# ● Create two points objects from Point namedtuple
# ● Write a function to get distance between that two points


from collections import namedtuple
Point = namedtuple("Point", "x,y")


def find_distance(point1, point2):

    dist_x = point1.x - point2.x
    dist_y = point1.y - point2.y

    distance = (dist_x ** 2 + dist_y ** 2) ** 0.5
    return distance


def find_perimeter(point1, point2, point3):
    if point1.x == point2.x == point3.x or point1.y == point2.y == point3.y:
        raise Exception("It's impossible to make a triangle!")

    side1 = find_distance(point1, point2)
    side2 = find_distance(point2, point3)
    side3 = find_distance(point3, point1)
    perimeter = side1 + side2 + side3
    return perimeter


point_1 = Point(56, 41)
point_2 = Point(56, 80)
point_3 = Point(56, 21)
print(find_distance(point_1, point_2))
print(find_perimeter(point_1, point_2, point_3))


