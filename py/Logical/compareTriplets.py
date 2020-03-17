# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for number in ar:
        sum += number
    return sum

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = aVeryBigSum(ar)
print(result)