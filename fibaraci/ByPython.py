# Không dùng dệ quy
# def fibonancci(n):
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
def fibonancci(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return fibonancci(n -1) + fibonancci(n -2)


while True:
    try:
        n = int(input('Enter number of element: '))
        for i in range (0,n):
            print(fibonancci(i))
        break
    except ValueError:
        print('Please enter a number')
