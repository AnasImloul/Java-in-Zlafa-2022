def can_balance(seq):
    # balancing the sequences means that in the end the count of W and B is the same
    # you can notice that after any operation the difference between W and B is unchanged
    # so we can only balance the sequence if the number of W and B is the same since the start
    return seq.count("W") == seq.count("B")


seq = input()
print(int(can_balance(seq)))