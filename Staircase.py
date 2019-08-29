def Staircase(n):
    space = n-1
    for num in range(n):
        hash = num +1
        s = ' '* space + '#'*hash
        space-=1
        print(s)





print(Staircase(4))