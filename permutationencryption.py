# this function takes a string with the same length as a permutation and returns the encrypted string
def partial_encrypt(string, permutation, length):
    # text: the text to encrypt
    # permutation: the permutation to use
    # length: the length of the permutation and the length of the text
    # return: the encrypted text
    result = ""
    for i in range(length):
        result += string[permutation[i] - 1]
    return result


def encrypt(text, permutation, length):
    # text: the text to encrypt
    # permutation: the permutation to use
    # return: the encrypted text
    result = ""
    for i in range(0, len(text), length):
        string = text[i:i+length]
        if len(string) < length:
            string += " " * (length - len(string))
        result += partial_encrypt(string, permutation, length)
    return result


def main():
    line = input()
    while line != "0":
        # read the permutation from the input line and convert it to a list of integers
        # make sure to decrement each number by 1 since the permutation is 1-indexed
        permutation = [int(i) for i in line.split()[1:]]
        text = input()
        print("'" + encrypt(text, permutation, len(permutation)) + "'")
        line = input()


main()
