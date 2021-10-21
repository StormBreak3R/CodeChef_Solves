def power(n, p):
    if p == 0:
        return 1
    else:
        return n * power(n, p-1)


n = int(input("Enter a number: "))
p = int(input("Enter a power value: "))

x = power(n, p)
print("Ans: ", x)
