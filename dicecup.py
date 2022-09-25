# read N & M from the input line
# input().split() splits the input line into a list of strings that are separated by spaces
# map(int, input().split()) converts the list of strings into a list of integers
N, M = map(int, input().split(" "))
# N must be smaller than M
N, M = sorted([N, M])
# then print the numbers from N+1 to M+1 inclusive
for i in range(N+1, M+2):
    print(i)