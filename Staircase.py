def staircase(n):
    space = n-1
    for num in range(n):
        hash = num +1
        s = ' '* space + '#'*hash
        space-=1
        print(s)




staircase(4)