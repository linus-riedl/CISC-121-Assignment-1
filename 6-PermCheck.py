def solution(A):
    found = set() # initialize empty set to store found integers
    l = len(A) # find the length of the input array, to be used in the loop
    for a in A: # iterate through every element in the input array
        if a>l or a<1 or a in found: # if the element is not in the range (1..n) or it appears more than once
            return 0 # it is not a permutation
        found.add(a) # update the set of found integers
    return 1 # return 1 if the entire loop passed, and it therefore is a permutation