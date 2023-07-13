def count(arr):
    count=0
    maximum=float("-inf")
    for i in arr:
        if i > maximum:
            maximum=i
    for i in arr:
        if i== maximum:
            count=count+1
    return  len(arr)-count
print(count(list(map(int,input().split()))))
