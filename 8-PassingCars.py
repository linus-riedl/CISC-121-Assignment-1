def solution(A):
    # initialize 2 counters
    oncoming = 0
    total = 0

    # iterate through each car's direction
    for direction in A:
        if direction == 1:
            total+=oncoming # this car will pass all oncoming cars that were ahead of it
        else:
            oncoming+=1 # update the oncoming counter
        if total>1_000_000_000:
            return -1 # return -1 if the size limit of the problem is exceeded.
    # return the total number of passing cars.
    return total