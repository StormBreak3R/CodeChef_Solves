x, y = map(float, input().split())

if x % 5 == 0 and x+0.5 <= y:
    y = ((y-x)-0.5)

print("%.2f"%y)