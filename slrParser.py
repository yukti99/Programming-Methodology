#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yukti
#
# Created:     14-09-2018
# Copyright:   (c) yukti 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# Stack implemetation
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def display(self):
        print self.items

"""
SIMPLE LR PARSER FOR A GRAMMAR IN PYHTON
E -> E + T | T
T -> T * F | F
F -> (E)| P
P -> 0|1|2|3|4|5|6|7|8|9
"""
# exp = 4+5*6
# $ - empty string
s = Stack()
e = Stack()
s.push('$')
#e.push('$')
exp = str(raw_input("Enter the Expression to check : "))
"""
y = ""
for i in exp:
    if i.isdigit():
        y += "P"
    else:
        y += i
exp = y
"""
print "Expression = ",exp

rev = exp[::-1]
for i in rev:
    e.push(i)
op = ['+','-','*','/','%','^']
op1 = ['+','-']
op2 = ['*','/','%']
op3 = ['^']
temp = ""
print "s = ",
s.display()
print "e = ",
e.display()
def ReduceP(s):
    s.pop()
    s.push('F')
    print "Reduce F -> P"
    s.display()
    s.pop()
    s.push('T')
    print "Reduce T -> F"
    s.display()
value = 0
top = e.peek()
if top in op:
    print "REJECT!!"
    exit()

while(not e.isEmpty()):
    i = e.peek()
    if (i.isdigit()):
        s.push(e.pop())
        print "Shifting : "
        print "s = ",
        s.display()
        print "e = ",
        e.display()
        continue
    if (i in op2):
        l = e.size()
        if(l==1):
            print "REJECT!!"
            exit()
        x = s.pop()
        y = e.pop()
        z =  e.pop()
        if(y not in op):
            print "REJECT!!"
            exit()
        if(i=='*'):
            value = int(x)*int(z)
            value = str(value)
            s.push(value)
            print "Reduce T -> T * F"
        if(i=='/'):
            if int(z) == 0:
                print "Division by Zero Error!!"
                print "REJECT!!"
                exit()
            value = int(x)/int(z)
            value = str(value)
            s.push(value)
            print "Reduce T -> T / F"
        if(i=='%'):
            value = int(x)%int(z)
            value = str(value)
            s.push(value)
            print "Reduce T -> T % F"
        print "s = ",
        s.display()
        print "e = ",
        e.display()
    if (i in op1):
        l = e.size()
        if(l==1):
            print "REJECT!!"
            exit()
        x = e.pop()
        y = e.pop()
        if(y in op):
            print "REJECT!!"
            exit()
        s.push(x)
        s.push(y)
        print "s = ",
        s.display()
        print "e = ",
        e.display()
        continue
    if  (i in op3):
        l = e.size()
        if(l==1):
            print "REJECT!!"
            exit()
        x = e.pop()
        y = e.pop()
        if(y in op):
            print "REJECT!!"
            exit()
        s.push(x)
        s.push(y)
        print "s = ",
        s.display()
        print "e = ",
        e.display()
        z = e.peek()
        if(z not in op):
            print "REJECT!!"
            exit()
        if(z in op3):
            continue
        else:
            while(1):
                m = s.pop()
                n = s.pop()
                value = int(m)**int(n)
                value = str(value)
                h = s.peek()
                if(h != '^'):
                    break
                s.push(value)
                print "Reduce F -> P ^ F"
                print "s = ",
                s.display()
                print "e = ",
                e.display()





l = s.size()
top = s.peek()
if (l==2) :
    print "Final Value = ",s.pop()
    exit()
if top in op:
    print "REJECT!!"
    exit()
while (not s.isEmpty()):
    l = s.size()
    if(l == 2):
        print "Final Value = ",s.pop()
        break
    if(l<4):
        print "REJECT!!"
        exit()
    x = s.pop()
    y = s.pop()
    z = s.pop()
    if(y == '+'):
        value = int(x)+int(z)
        value = str(value)
        s.push(value)
        print "Reduce E -> E + T"
    if(y == '-'):
        value = int(x)-int(z)
        value = str(value)
        s.push(value)
        print "Reduce E -> E + T"
    print "s = ",
    s.display()



"""
E -> E + T | E - T | T
T -> T * F | T / F | T % F | F
F -> P ^ F | P
P -> 0|1|2|3|4|5|6|7|8|9  """




"""
while(not e.isEmpty()):
    i = e.peek()
    print i
    if (i == "P") :
        s.push(e.pop())
        print "s = ",
        s.display()
        print "e = ",
        e.display()
        continue
    if (i in op2):
        j = s.peek()
        if j == "P":
            ReduceP(s)
        l = e.size()
        if(l<2):
            print "REJECT!!"
            exit(0)
        s.push(e.pop())
        s.push(e.pop())
        s.display()
        e.display()
        print "Reduce T -> T*F"


        break
    if (i in op1):

        ReduceP(s)
        s.pop()
        s.push('E')
        print "Reduce  E -> T"
        s.display()

"""

# 5+4^3^2-9/3


















