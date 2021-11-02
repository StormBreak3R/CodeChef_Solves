array = [11, 15, 25, 77, 27, 45, 30, 1, 9, 3, 7]


def max_product_pair(arr):
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] > max_product:
                max_product = arr[i]+arr[j]
                pairs = arr[i], arr[j]
    print(list(pairs))
    print(max_product)


max_product_pair(array)
