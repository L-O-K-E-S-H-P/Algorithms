#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. 


def bubble_sort(arr):
  for i in range(0,len(arr)-1):
    for j in range(len(arr)-1):
      if(arr[j]>arr[j+1]):
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr
arr=[5,3,8,6,7,1,2]
print("The Unsorted Array is:",arr)
print("The Sorted Array is:",bubble_sort(arr))


''''
Output:
The Unsorted Array is: [5, 3, 8, 6, 7, 1,2]
The Sorted Array is: [1,2, 3, 5, 6, 7, 8]
'''
