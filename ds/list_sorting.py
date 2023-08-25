import time

def bubble(arr):
    print("BUBBLE SORT")
    start_time = time.time()
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                print(arr)
    print(f"EXECUTION TIME: {round(time.time() - start_time, 4)}s")
    return arr

def insertion(arr):
    print("INSERTION SORT")
    start_time = time.time()
    for i in range(1, len(arr) - 1):
        tmp = arr[i]
        j = i - 1
        while(j >= 0 and tmp < arr[j]):
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
        print(arr)
    print(f"EXECUTION TIME: {round(time.time() - start_time)}s")
    return arr         


my_numbers = [4000, 1, 19, 888, 11, 2, 5, 100]

print(bubble(my_numbers))
print(insertion(my_numbers))