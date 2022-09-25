from math import sqrt

# Returns the smallest divisor of n
def smallest_divisor(q):
    if q % 2 == 0:
        return 2
    for i in range(3, int(sqrt(q)) + 1, 2):
        if q % i == 0:
            return i
    return q


# returns True if n is only divisible by a single prime
# example: solve(125) -> True since 125 = 5^3
# example: solve(126) -> False since 126 = 2 * 3^2
def solve(q):
    # if q is 1 then it's not prime
    if q == 1:
        return False
    # get the smallest divisor of q
    a = smallest_divisor(q)
    # repeat the process on q until it's equal to 1
    while q != 1:
        # if q is not divisible by a then there is more than one prime factor
        if q % a != 0:
            return False
        # divide q by a
        q = q // a
    return True


q = int(input())
print("yes" if solve(q) else "no")