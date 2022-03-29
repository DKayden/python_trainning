from random import randint

arr = []

while True:
    try:
        n = int(input("Enter number of element in array: \n"))
        break
    except ValueError:
        print('Please enter a number')
# print('Number: ' + str(n))
for i in range(0, n):
    # ele = int(input())
    ele = randint(0, n)
    arr.append(ele)
    print(ele)
print("Unsort array: " + str(arr))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print('Sorted array: ' + str(arr))
# numberSorted = sorted(arr)
# print("Sorted array: " + str(numberSorted))