def solution(A):
    found = set()
    l = len(A)
    for a in A:
        if a>l or a<1 or a in found:
            return 0
        found.add(a)
    return 1