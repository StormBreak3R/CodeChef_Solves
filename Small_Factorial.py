def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)


for i in range(int(input())):
    x = int(input())
    print(factorial(x))
