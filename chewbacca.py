# a function that returns the parent of a node
def parent(index, k):
    index = index - 1
    return (index - 1) // k + 1


# a function that returns the depth of a node
def depth(index, k):
    # the depth of the root is 0
    if index == 1:
        return 0
    # the depth of a node is equal to the depth of its parent incremented by 1
    return depth(parent(index, k), k) + 1


def distance(i, j, k):
    # the distance between a node and itself is 0
    if i == j:
        return 0
    # compute the depth of the nodes
    d1, d2 = depth(i, k), depth(j, k)
    # move the node with the greater depth up one level to its parent
    # now the distance is equal to the distance between the parent and the other node plus 1
    if d1 > d2:
        return distance(parent(i, k), j, k) + 1
    elif d2 > d1:
        return distance(i, parent(j, k), k) + 1
    # if the depths are equal then move both nodes up one level to their parents
    # now the distance is equal to the distance between the parents plus 2
    return distance(parent(i, k), parent(j, k), k) + 2


N, K, Q = map(int, input().split())
for query in range(Q):
    a, b = map(int, input().split())
    print(distance(a, b, K))


