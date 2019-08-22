def plusMinus(arr):
    pos_val = 0
    neg_value = 0
    zero_value = 0
    for element in arr:
        if element>0:
            pos_val+=1
        elif element<0:
            neg_value+=1
        elif element==0:
            zero_value+=1

    pos_frac = ("{:.6f}".format(pos_val/len(arr)))
    neg_frac = ("{:.6f}".format(neg_value/len(arr)))
    zero_frac = ("{:.6f}".format(zero_value/len(arr)))

    print(pos_frac)
    print(neg_frac)
    print(zero_frac)

arr=[-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))