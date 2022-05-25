import fx
import pr
import series

# print(fx.sqfl(1000))
# print(fx.sqce(1000))
# print(fx.sqrt(1000))

# print(fx.sqrt(24))
# print(fx.sqrt(25))
# print(fx.sqrt(26))

# print(fx.sqrt(2197830248723948237498237493284729384723984754905603492856720398457092348570982345692734))

# print(fx.sq(5))

# print(fx.mod10(123123891023129038120938121))

# print(pr.nextNum(1))
# print(pr.nextNum(3))
# print(pr.nextNum(7))
# print(pr.nextNum(9))
# print(pr.nextNum(1231238910231290381209381218975239045629374569234856923487502349752304570943785508230487))


# series.inc(1, 2, 100)
# series.sqinc(1, 1, 1000)

#series.t1_sqinc(1, 1, 1000)
#series.t1_sqinc(1, 1, 100000)
#series.t1_sqinc(10000000000000000000000, 1, 1000)

#t = 9999
t = 1000000000000000000000000000
print("Until " + str(pr.checkUntilSq(t)))
print("SQ__: " + str(fx.sq(pr.checkUntilSq(t))) + " " + str(pr.checkUntilSq(t)))
print("SQCE: " + str(fx.sq(pr.checkUntilSqCe(t))) + " " + str(pr.checkUntilSqCe(t)))
print("SQFL: " + str(fx.sq(pr.checkUntilSqFl(t))) + " " + str(pr.checkUntilSqFl(t)))
# div in sqrt value is NOT of significance 
# 1000000000000000000000000000
# -> 1000000000000013069988134912 31622776601684
# -> 999999999999949848069537792 31622776601683