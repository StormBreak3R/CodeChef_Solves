#  GCD
#  using Euclidean Algorithm

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

ans = gcd(x, y)
print("GCD is:", ans)