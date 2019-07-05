def even_odd(A):
    next_even, next_odd = 0, len(A)-1

    while(next_even < next_odd):
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd],A[next_even]
            next_odd -= 1


q = [2,45,6,3,2,5,7,0,-1,3,0]
even_odd(q)
print(q)

