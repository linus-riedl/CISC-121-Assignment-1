def solution(N, A):
    maximum=0
    minimum=0
    counters=[0]*N # initialize array of N zeros

    for a in A:
        if a ==N+1:
            minimum=maximum # instead of updating all counters at once (this would be quadratic time), just update the minimum
        else:
            index = a-1 #a-1 because index starts at 0
            # update the counter if it was under the minumum, then add 1 to it
            counters[index]=max(counters[index], minimum)+1

            # update the maximum if this counter has passed it
            maximum = max(maximum, counters[index])

    # for each counter, it will stay the same if it's above the minimum, otherwise it equals the mimimum.
    return [max(counter, minimum) for counter in counters]