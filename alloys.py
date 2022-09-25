def solve(c):
    # let z be minimum since it doesn't affect hardness
    # if c > 1, then set it to 1 since x + y = c and x + y <= 1
    # to maximize the hardness it's best to set z to 0 since z has no effect on hardness
    # and let x and y be equal to c / 2
    # since x * y is maximized when x = y
    if c > 1: c = 1
    # x = c/2, y = c/2 -> hardness = x*y = c^2/4
    return c*c/4

c = float(input())
print(solve(c))
