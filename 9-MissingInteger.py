def solution(A):
    A = set(A) # convert input array to a set
    for i in range(1,len(A)+2): # answer must be between 1 and n+1 (because 1 is the lowest possible positive integer, and n+1 is the worst case where the array contains all integers from 1 to n)
        if i not in A: # if the number is not in the set, it is the smallest possible answer
            return i # so, return it