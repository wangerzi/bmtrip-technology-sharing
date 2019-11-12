arr = [1, 1]
day = 12

for i in range(2, day):
    arr.append(arr[i - 2] + arr[i - 1])
print(arr)
