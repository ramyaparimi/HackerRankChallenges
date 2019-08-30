def miniMaxSum(arr):
    total_array_sum = []
    for i in range(len(arr)):
        popped_element = arr.pop(i)
        sum_new_arr = sum(arr)
        total_array_sum.append(sum_new_arr)
        arr.insert(i,popped_element)

    print(min(total_array_sum), max(total_array_sum))






miniMaxSum([1, 2, 3, 4, 5])