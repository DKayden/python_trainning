# Không dùng dệ quy
# def  fibonacci(n):
#     a = 0
#     b = 1
#     c = 1

#     if n < 0:
#         return -1
#     elif n == 0 or n == 1:
#         return n
#     else:
#         for i in range (2,n):
#             a = b
#             b = c
#             c = a + b
#         return c


#Dùng đệ quy
def  fibonacci(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return  fibonacci(n -1) +  fibonacci(n -2)

arr = []
while True:
    try:
        n = int(input('Enter number of element: '))
        for i in range (0,n):
            arr.append(fibonacci(i))
        print(arr)
        break
    except ValueError:
        print('Please enter a number')
