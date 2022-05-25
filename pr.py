import fx

def nextNum(num):
    lastDigit = fx.mod10(num)
    switcher={
        1: 2,
        3: 4,
        7: 2,
        9: 2
    }
    ret = fx.add(num, switcher.get(lastDigit))
    return ret


def checkUntilSq(num):
    #Check number until the sqrt is reached
    return fx.sqrt(num)

def checkUntilSqCe(num):
    #Check number until the sqce is reached
    return fx.sqce(num)

def checkUntilSqFl(num):
    #Check number until the sqfl is reached
    return fx.sqfl(num)
