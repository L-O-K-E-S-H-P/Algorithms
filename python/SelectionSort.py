def selection_sort(L):
    for i in range(len(L)-1):
        min_index=i
        for j in range(i+1,len(L)-1):
            if L[min_index]>L[j]:
                min_index=j
        L[i],L[min_index]=L[min_index],L[i]
L=[3,2,34,14,56,12,19,67,45]
print(L)
selection_sort(L)
print(L)
