# Python Program for Linear Search
'''
A simple approach is to do linear search, i.e

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
'''
 def search(arr,x):
    for i in range(len(arr)):
      if arr[i]==x:
        return i
     return -1
  
 '''The time complexity of above algorithm is O(n).'''
 '''
 Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].
'''
