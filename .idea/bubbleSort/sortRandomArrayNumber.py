import random

arr = []
n = int(input("Enter number of array: \n"))

for i in range(0, n):
    # ele = int(input())
    ele = random.randint(0, n)
    arr.append(ele)
print("Unsort array: " % arr)
for i in len(arr):
    for j in len(arr)-1:
        if arr[j - 1] > arr[i]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
print("Sorted array: " % arr)
