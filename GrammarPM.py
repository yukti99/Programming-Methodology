#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yukti
#
# Created:     07-09-2018
# Copyright:   (c) yukti 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# BNF GRAMMAR TESTING  CODE -1
"""
E -> E + T | E - T | T
T -> T * F | T / F | T % F | F
F -> P ^ F | P
P -> 0|1|2|3|4|5|6|7|8|9

Eg : 5+4-3
"""
import re
pattern = r"^[+|-]*\d+$"

def check_output(s):
    if(s.isalpha()):
        return False
    for i in s:
        if i in ['^','*','/','%','+'] :
            return False
    if(s[0]=='-' and '-' not in s[1::]):
        return True
    elif ('-' in s[1::]) :
        return False
    return True




def  bracket_check(exp):
    c = 0
    if(exp.count('(')!=exp.count(')')):
        return False
    for i in exp:
        if(i=='('):
            c+=1
        elif (i==')'):
            c-=1
        elif (c<0):
            return False
    return True

def find_value(exp):
    if(re.match(pattern,exp)):
        return exp

    l = list(exp)
    length = len(l)
    s = ""
    value=0
    ans = 0
    while(length!=1):
        # ^ is right associative
        if '^' in l:
            rev = l[::-1]
            for i in range(len(rev)):
                if (rev[i]=='^'):
                    del rev[i]
                    ans = int(rev[i]) ** int(rev[i-1])
                    del rev[i]
                    rev[i-1] = str(ans)
                    length-=2
                    l = rev[::-1]
                    s+=''.join(l)
                    print "Using Rule-F"
                    print s
                    if(check_output(s)):
                        value = int(s)
                    s=""
                    ans = 0
                    break
        # *,/,% are left associative
        elif '*' in l or '/' in l or '%' in l:
            for i in  range(len(l)):
                if (l[i]=='*'):
                    del l[i]
                    ans = int(l[i-1]) * int(l[i])
                    del l[i]
                    l[i-1] = str(ans)
                    length-=2
                    s += ''.join(l)
                    print "Using Rule-T"
                    print s
                    if(check_output(s)):
                        value = int(s)
                    s = ""
                    ans = 0
                    break
                elif (l[i]=='/'):
                    del l[i]
                    ans = int(l[i-1]) / int(l[i])
                    del l[i]
                    l[i-1] = str(ans)
                    length-=2
                    s += ''.join(l)
                    print "Using Rule-T"
                    print s
                    if(check_output(s)):
                        value = int(s)
                    s = ""
                    ans = 0
                    break
                elif (l[i]=='%'):
                    del l[i]
                    ans = int(l[i-1]) % int(l[i])
                    del l[i]
                    l[i-1] = str(ans)
                    length-=2
                    s += ''.join(l)
                    print "Using Rule-T"
                    print s
                    if(check_output(s)):
                        value = int(s)
                    s = ""
                    ans = 0
                    break
        # +,- are left associative
        elif '+' in l or '-' in l:
            for i in  range(len(l)):
                if (l[i]=='+'):
                    del l[i]
                    ans = int(l[i-1]) + int(l[i])
                    del l[i]
                    l[i-1] = str(ans)
                    length-=2
                    s += ''.join(l)
                    print "Using Rule-E"
                    print s
                    if(check_output(s)):
                        value = int(s)

                    s = ""
                    ans = 0
                    break
                elif (l[i]=='-'):
                    del l[i]
                    ans = int(l[i-1]) - int(l[i])
                    del l[i]
                    l[i-1] = str(ans)
                    length-=2
                    s += ''.join(l)
                    print "Using Rule-E"
                    print s
                    if(check_output(s)):
                        value = int(s)
                    s = ""
                    ans = 0
                    break
    return value


exp = str(raw_input("Enter the Expression : "))
print "The Expression : "+exp
# 5+3*2^3^2/3%9
op = ['^','*','/','%','+','-']
P = ['0','1','2','3','4','5','6','7','8','9']
F = ['^']
T = ['*','/','%']
E = ['+','-']
# to check for valid Expressions
if exp[0] == '+':
    exp = exp[1::]
if exp[0] == '-':
    exp = '0'+exp

if exp[0] in op or exp[len(exp)-1] in op:
    print("Invalid Expression! Ending...")
    exit()

b = ['(',')']
for i in range(len(exp)):

    if(exp[i] not in op and exp[i] not in P and exp[i] not in b):
        print("Invalid Expression! Ending...")
        exit()

    if (exp[i] in E):
        if ((exp[i+1] not in P) or (exp[i-1] not in P)):
            if (exp[i+1] not in b) and (exp[i-1] not in b) :
                print("Invalid Expression! Ending...")
                exit()
    elif (exp[i] in T):
        if ((exp[i+1] not in P) or (exp[i-1] not in P)):
            if (exp[i+1] not in b) and (exp[i-1] not in b) :
                print("Invalid Expression! Ending...")
                exit()

    elif (exp[i] in F):
        if ((exp[i+1] not in P) or (exp[i-1] not in P)):
            if (exp[i+1] not in b) and (exp[i-1] not in b) :
                print("Invalid Expression! Ending...")
                exit()
    elif ('(' in exp):
        if ( not bracket_check(exp)):
            print("Invalid Expression! Ending...")
            exit()
print "The Expression is Valid!\n"
# if expression has brackets,this funtion evaluates all the brakcets first and return exp without any brackets
def has_brackets(exp):
    print "Solving brackets first.."
    b = list(exp)
    e = ""
    v=0
    n = ""
    i=0
    n=""
    while(i<len(b)):
        if (i == exp.rfind('(')):
            i+=1
            while(b[i]!=')'):
                n += b[i]
                i+=1
            print n
            i+=1
            v = str(find_value(n))
            if('-' in v):
                v = '0'+v
            e += v
        if(i>=len(b)):
            break
        e +=b[i]
        i+=1
    print e

    if('(' in e):
        e = has_brackets(e)
    return e


# if the whole expression is inside the brackets
#exp = "(5+(4*(3-2))-(2*3)+2)*(3/3)"


print "Expression = ",exp
if ('(' in exp):
    e = has_brackets(exp)
    print "After Solving all brackets :",e
    if(re.match(pattern,e)):
        v = e
    else:
        v =  find_value(e)
    print "Final Value of Expression : ",v
else:
    v =  find_value(exp)
    print "Final Value of Expression : ",v
