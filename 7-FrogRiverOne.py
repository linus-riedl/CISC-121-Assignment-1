def solution(X, A):
    # initialize empty set to keep track of leaves, and a counter for the amount of positions found
    found = set()
    counter = 0

    for i in range(len(A)):
        # find the position of the leaf at index i
        leaf = A[i]
        if leaf not in found:
            # if the position of this leaf hasn't been found yet, add it to the list of found leaves and update the counter
            found.add(leaf)
            counter+=1

        # if all leaves have been found, return the index at which they are all found
        if counter==X:
            return i
    # if all leaves have been checked and there is still no path, return -1
    return -1  