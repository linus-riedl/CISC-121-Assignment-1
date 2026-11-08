def solution(X, A):
    found = set()
    counter = 0

    for i in range(len(A)):
        leaf = A[i]
        if leaf not in found:
            found.add(leaf)
            counter+=1
        if counter==X:
            return i
    return -1