array = [11, 15, 25, 77, 27, 45, 30, 1, 9, 3, 7]


def finding_pair(arr, n):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == n:
                print(i, j)


finding_pair(array, 10)
