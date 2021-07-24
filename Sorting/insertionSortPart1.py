def insertionSort1(n, arr):
    # Write your code here
    sorted_ele = arr[-1]
    for i in reversed(range(0,n-1)):
        if(arr[i] > sorted_ele):
            arr[i+1] = arr[i]
            print(*arr)
            if (i==0):
                arr[i]=sorted_ele
                print(*arr)
        elif(arr[i] <= sorted_ele):
            arr[i+1] = sorted_ele
            print(*arr)
            break
