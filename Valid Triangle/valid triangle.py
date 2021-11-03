#  FLOW013
"""
Write a program to check whether a triangle is valid or not,
when the three angles of the triangle are the inputs.
A triangle is valid if the sum of all the three angles is equal to 180 degrees.
"""

for i in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] + a[1] + a[2] == 180:
        print("YES")
    else:
        print("NO")
