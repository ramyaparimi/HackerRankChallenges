def simpleArraySum(ar):
    total = 0
    for i in ar:
        total = total+i
    return total


ar = [1,2,3,4,10,11]
print(simpleArraySum(ar))