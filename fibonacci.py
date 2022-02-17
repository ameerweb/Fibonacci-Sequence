# User should input number
num = int(input())


def fibonacci(n):
    # creating a variables that will hold the first and second value
    a = 0
    b = 1
    print(a)
    print(b)
    # for loop start with 1 and end with user input - 1
    for i in range(1, num-1):
        c = a + b
        # assigning the value of a to b and the value of b to c
        a, b = b, c


fibonacci(num)


# for more details about this function read the readme.md file
# made with ❤ by Ameer Almughalis (github.ameerweb)
