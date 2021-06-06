for x in range(151):
    print(x)

for x in range(5,1000, 5):
    print (x)

for x in range(1,100):
    if x  % 5 ==0:
        print ("Coding Dojo")
        continue
    print(x)

def addOdds():
    total = 0
    for x in range(500000):
        if x % 2 == 1:
            total += x
    print(total)

print(addOdds())

for x in range(2018, 0, -4):
    print(x)


lowNum = 2
highNum = 13
mult = 3
for mult in range(lowNum, highNum):
    if mult % 3 == 0:
        print(mult)