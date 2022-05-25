import fx

# increment (start, increment by, x times)
def inc(num, by, xtimes):
    cnum = num
    for x in range(xtimes):
        cnum = fx.add(cnum, by) #increment
        print(cnum)


# square increment (start, increment by, x times)
def sqinc(num, by, xtimes):
    
    for x in range(xtimes):
        cnum = fx.sq(num) #square
        num = fx.add(num, by) #increment
        print(cnum)


# test 1 - square increment (start, increment by, x times)
def t1_sqinc(num, by, xtimes):
    
    for x in range(xtimes):
        cnum = fx.sq(num) #square
        print(num, cnum)
        num = fx.add(num, by) #increment
        