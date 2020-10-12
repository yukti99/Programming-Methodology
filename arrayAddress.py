#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      yukti
#
# Created:     02-11-2018
# Copyright:   (c) yukti 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
def synCheck(exp):
    if ('[' not in dec  or ']' not in dec):
    	return 0
    c = 0
    no = 0
    for i in exp:
    	if (i == '['):
            c += 1
	    no +=1
        if (i == ']'):
            c -= 1
    if (c != 0):
        return (0,no)
    return (1,no)

code = raw_input("Enter the array declaration :")
if ('['in code ):
    if (']'not in code):
        print "Unbalanced Parenthesis"
        exit()
length = len(code)
if (code[length-1] != ';'):
	print("Syntax Error : Missing Semicolon!")
	exit()
l = code.strip(";").split()
dtype = str(l[0])
size = len(l)
types = {"int":4,"float":4,"double":8}
if (dtype not in types.keys()):
    print ("Invalid data type Error!!")
    exit(0)
else:
	E = types[dtype]


dec = str(l[1])
if (" "in dec):
    print "Invalid Array Declaration"
    exit()

name = ""
for i in dec:
    if (i=='['):
        break
    name+=i

if (len(dec) <=1):
    print ("Invalid Array Declaration !")
elif (synCheck(dec)[0] == 0):
    print ("Syntax Error! Wrong parenthesis for array declaration")
else:
    # base address
    a = 123456
    b = synCheck(dec)[1]
    if (b == 1):
        for i in range(len(dec)):
            if (dec[i] == '['):
                st = i
            if (dec[i] == ']'):
                end = i
                d = dec[st+1:end]
                if (d) and (d!='0'):
                    asize = int(d)
                    break
                else:
                    print("Invalid Declaration!")
                    exit()

        print "The Array name : ",name
        print "Array of size = ",asize
        print "Type = ",dtype
        I = int(raw_input("Enter the Lower index = "))
        if (I>asize):
            print "Array index out of bound !!"
            exit()
        lb = int(raw_input("Enter the Lower Bound = "))
        ub = lb+asize-1
        VO  = a + (I-lb)*E
        print "The Address of the block = ",a
        print "The Virtual Origin  = ",VO
    else:
        s = []
        for i in range(len(dec)):
            if (dec[i] == '['):
                st = i
            if (dec[i] == ']'):
                end = i
                d = dec[st+1:end]
                if (d) and (d != '0'):
                    s.append(int(d))
                else:
                    print("Invalid Declaration!")
                    exit()
        print "Name of array = ",name
        print "Array of sizes = ",s[0],s[1]
        print "Type =",dtype
        I = int(raw_input("Enter the Lower index = "))
        J = int(raw_input("Enter the Upper index = "))
        if (0<=I<s[0] and 0<=J<s[1]):
            lb1 = int(raw_input("Enter the Lower Bound for rows = "))
            lb2 = int(raw_input("Enter the Lower Bound for columns = "))
            ub1 = lb1+s[0]-1
            ub2 = lb2+s[1]-1
            r = ((ub2-lb2) + 1)*E
            VO = a + (I-lb1)*r + (J-lb2)*E
            print "The Address of the block = ",a
            print "The Virtual Origin  = ",VO
        else:
            print "Array index out of bound !!"
            exit()













































