base_repr = {36: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
             13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o',
             25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}


def convert(number, base):
    # convert number from decimal string to a given base
    if base == 1:
        # base 1 is a special case
        # it's just the length of the number
        # so we can just return the length of the number
        # if the number is not all 1's then it's invalid
        if number.count("1") != len(number):
            return -1
        return len(number)
    else:
        # convert the number to the given base
        # use the int function to convert the number to the given base
        return int(number, base)


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


def div(x, y):
    if y == 0:
        return -1
    return x / y


ops = {"+": add, "-": sub, "*": mul, "/": div}


def valid_bases(expression):
    bases = ""
    # expression example: 1 + 1 = 2
    x, op, y, equal, z = expression.split()

    # operator is the function to use to calculate the result
    # for example, if the operator is + then we use the add function
    operator = ops[op]
    for base in range(1, 36+1):
        # convert the numbers from base to decimal
        a = convert(x, base)
        b = convert(y, base)
        c = convert(z, base)

        # if any of the numbers are invalid then skip this base
        # if they are invalid they will be -1
        if a < 0 or b < 0 or c < 0:
            continue

        # calculate the result
        # if the result is equal to the result in the expression
        # then the base is valid
        # and add it to the bases string
        if operator(a, b) == c:
            bases += base_repr[base]

    # if bases is empty then there are no valid bases
    if bases == "":
        return "invalid"
    return bases


for test in range(int(input())):
    exp = input()
    print(valid_bases(exp))