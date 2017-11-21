import re


solution2 = '^(0|1*0)*$'
solution3 = '^(0|(1(01*0)*1))*$'
solution4 = '^(0|(1(0|1+0)+0)*)*$'
solution5 = '^(0|1(10)*(0|11)(01*01|01*00(10)*(0|11))*1)+$'
solution5a = '^(0|((1(10)*(0|11))((01*0)1|((01*0)0(10)*(0|11)))*1))*$'
solution6 = '^(0|((1(1|((0(0|(1+0)))+1)))+0))*$'
solution7 = '^(0|(1((0(01)*00)|((0(01)*1)(11(01)*1)*((10)|(11(01)*00))))*(1|((0(01)*1)(11(01)*1)*0))(((01*0)(11(01)*1)*0)|(((01*0)(11(01)*1)*((10)|(11(01)*00)))((0(01)*00)|((0(01)*1)(11(01)*1)*((10)|(11(01)*00))))*(1|((0(01)*1)(11(01)*1)*0))))*1))+$'





rgx = re.compile(solution7)
fails = 0
for num in range(0,1001):
#    print('Testing for: '+str(num))
    if (rgx.match(bin(num)[2:]) is not None) == (num%7 == 0):
        continue
    else:
        print(bin(num)[2:])
        print(rgx.match(bin(num)[2:]) is not None)
        print(num%7 == 0)
        fails += 1
        print('test fails for ', num)

if fails > 0:
    print("There are", fails, "fails")
else:
    print("Tests pass")