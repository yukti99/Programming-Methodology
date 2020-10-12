#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yukti
#
# Created:     19-08-2018
# Copyright:   (c) yukti 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def is_var(s):
    if( 97<=ord(s[0])<=122 or 65<=ord(s[0])<=90):
        f=1
    else:
        return 0;
    for j in s:
        if (97<=ord(j)<=122) or (65<=ord(j)<=90) or (48<=ord(j)<=57) or ( ord(j)==95)  :
            continue
        else:
            f=0
            break
    if (f==1):
        return 1
    else:
        return 0

def is_int(s):
    f=1
    for i in s:
        if (48<=ord(i)<=57):
            continue
        else:
            f=0
            break
    if(f==1):
        return 1
    else:
        return 0

def is_float(s):
    c=0
    f=1
    if '.' not in s:
        return 0
    for i in s:
        if (48<=ord(i)<=57 ):
            continue
        if (i=='.'):
            c = c+1
            continue
        else:
            f=0
            break
    if (f==0 or c>=2):
        return 0
    else:
        return 1

def is_operator(s):
    op = ['+','-','*','/','%','++','--','=']
    f=1
    for i in s:
        if i not in op:
            f=0
            break
    if(f==1):
        return 1
    else:
        return 0




code = raw_input("Enter C line of code : ")
l = code.split(" ")
keywords = ["int","float","long","short","signed","double"]
key=[]
var = []
integer = []
fl =[]
operator = []
invalid = []
size = len(l)
if ( l[size-1] != ';') :
    print "Invalid Syntax!"
    exit()
del l[size-1]
a=b=c=d=e=f=0
for i in l:
        if i in keywords:
        	key.append(i)

        elif (is_var(i)):
        	if i not in var:
             		var.append(i)

        elif (is_int(i)):
        	if i not in integer:
            		integer.append(i)

        elif (is_float(i)):
        	if i not in fl:
            		fl.append(i)

        elif (is_operator(i)):
        	if i not in operator:
            		operator.append(i)

        else:
            invalid.append(i)

if (key):
	print "\nKeywords : ",
	for x in key:
		print x,


if (var):
    print "\nValid Identifiers : ",
    for x in var:
        print x,

if (integer):
    print "\nintegers : ",
    for x in integer :
        print x,

if (fl):
    print "\nfloat values : ",
    for x in fl:
        print x,

if (operator):
    print "\noperators : ",
    for x in operator:
        print x,


if (invalid):
	print "\nInvalid Identifiers : ",
	for x in invalid:
		print x,




