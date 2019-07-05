'''
List - Dynamically-resized

syntax for instantiating -
    [3,4,5,6]
    [1] + [0]*10
    list(range(100))

Basic operations -
    len(A)
    A.append(val)
    A.remove(val)
    A.insert(idx,val)

Checking if a value is present in the array
    val in A
    Complexity :- O(n) where n is the leath of the array

Key Methods -
    min(A)
    max(A)
    A.reverse() in-place
    reversed(A) return an iterator
    A.sort() in-place
    sorted(A) returns a copy
    del A[i] deletes the i-th element
    del A[i:j] removes the slice
    
    Binary Search or Bisection Search or Logarithmic Search for sorted array -
        bisect.bisect(A,val)
        bisect.bisect_left(A,val)
        bisect.bisect_right(A,val)

Slicing -
    A[i:j:k] with all of i,j and k is optional




-----------------------------------------------------------------------

List Comprehension  -
A succinct way to create lists
A list Comprehension  consists of
    1) an input sequence
    2) an iterator over the input sequence
    3) a logical contion over the iterator(optional)
    4) an expression that yeilds the elements of the derived list
Although list Comprehensions can always ve rewritten using map(), filter() and lambdas



'''

# bisect examples

from bisect import bisect_left 
  
def BinarySearch(a, x):
    a.sort()
    i = bisect_left(a, x) 
    print(i)
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
  
a  = [1, 2, 4, 4, 8] 
x = int(4) 
res = BinarySearch(a, x) 
if res == -1: 
    print(x, "is absent") 
else: 
    print("First occurrence of", x, "is present at", res) 

#------------------------------------------------------------------------

'''
Quick Sort after the reordering of array solution is known as Dutch national flag partitioning


'''