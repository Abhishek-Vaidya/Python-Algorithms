def Linearsearch(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
N = len(arr)
res = Linearsearch(arr , N , x);
if(res == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", res)