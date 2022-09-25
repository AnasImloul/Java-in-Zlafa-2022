pi = 3.14159


def area(a, b, theta):
    # given r = a*theta / 2pi + b in the polar coordinate system
    # the area of the sector is the integral of r * d(theta) from 0 to theta
    m = a / (2 * pi)
    c = b
    # r = m * theta + c
    # area = integral of 1/2 * r*r * d(theta) from 0 to theta
    # area = integral of 1/2 * (m * theta + c)*(m * theta + c) * d(theta) from 0 to theta
    # area = integral of 1/2 * (m*m * theta*theta + 2*m*c*theta + c*c) * d(theta) from 0 to theta
    return 1 / 2 * (m * m * theta * theta * theta / 3 + m * c * theta * theta + c * c * theta)


# find the value of x such that f(x) = y
def find(f, theta, a, b, low=0.0, high=2 * pi):
    # binary search
    m = (low + high) / 2
    # if the difference between the value of f(m) and y is less than 0.0000001
    # then return m
    if high - low < 1e-5:
        return m
    # if f(m) is less than y then the value of x is greater than m
    if f(a, b, m) < theta:
        return find(f, theta, a, b, low=m, high=high)
    # if f(m) is greater than y then the value of x is less than m
    else:
        return find(f, theta, a, b,low=low,high=m)


def solve(a, b, n):
    # the total area of the pizza is equal to area(a, b, 2pi)
    total_area = area(a, b, 2 * pi)
    reached = 0
    for i in range(n - 1):
        reached += total_area / n
        m = find(area, reached, a, b)
        print(m, 5)


a, b, n = map(float, input().split())
n = int(n)
solve(a, b, n)


