from math import sqrt


def distance(p, line):
    p1, p2 = line
    # if the line is horizontal
    # return the difference between the y coordinate of the point and the y coordinate of the line
    if p1[0] == p2[0]:
        return abs(p[0] - p1[0])
    # if the line is vertical
    # return the difference between the x coordinate of the point and the x coordinate of the line
    if p1[1] == p2[1]:
        return abs(p[1] - p1[1])
    # if the line is neither horizontal nor vertical
    # return the distance between the point and the line
    # using the equation of a line in the form y = mx + b
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - m * p1[0]
    return abs(m * p[0] - p[1] + b) / sqrt(m * m + 1)


def furthest(line, polygon):
    # return the furthest point in the polygon from a line
    # this is the point that is the furthest from this line
    # we can call it the diameter of the polygon along this line
    return max(distance(point, line) for point in polygon)


def solve(poly):
    lines = convert_lines(poly)
    # return the minimum of the diameters of the polygon
    return min(furthest(line, poly) for line in lines)


def convert_lines(poly):
    # return a list of all the lines in the polygon
    # the lines are represented as tuples of two points
    # we cycle through the points in the polygon and connect each point to the next point
    # the last point is connected to the first point
    # ex: [(1,2),(3,4)] -> [((1,2),(3,4)),((3,4),(1,2))]
    return [(x, y) for x, y in zip(poly, poly[1:] + [poly[0]])]


def main():
    n = int(input())
    poly = [tuple(map(float, input().split())) for _ in range(n)]
    print(round(solve(poly),3))


main()
