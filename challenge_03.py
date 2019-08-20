def aVeryBigsum(ar):
    total = 0
    for i in ar:
        total= total+i
    return total

n = 5
ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(aVeryBigsum(ar))
