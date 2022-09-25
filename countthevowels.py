vowels = "aeiou"


def count_vowels(string):
    # count the number of vowels in the string
    # use a for loop to iterate through the string
    # if the character is a vowel then add 1 to the count
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


string = input()
print(count_vowels(string))