#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yukti
#
# Created:     15-09-2018
# Copyright:   (c) yukti 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# STACK IMPLEMENTATION
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
        return self.items
    def string(self):
        return("".join(self.items))
    def displayRev(self):
    	return("".join(self.items[::-1]))

#-------------------------------------------------------------------------------

"""
SIMPLE LR PARSER FOR A GRAMMAR IN PYTHON
E -> E + T | E - T | T
T -> T * F | T / F | T % F | F
F -> P ^ F | P
P -> 0|1|2|3|4|5|6|7|8|9
"""
#-------------------------------------------------------------------------------
# DEFINING GRAMMAR TO BE CHECKED

grammar = {"E+T":'E',"E-T":"E","T":"E","T*F":"T","T/F":"T","T%F":"T","F":"T","P^F":"F","P":"F"}
g1 = {"E+T":'E',"E-T":"E","T":"E"}
g2 = {"T*F":"T","T/F":"T","T%F":"T","F":"T"}
g3 = {"P^F":"F","P":"F"}
P = "0123456789"
op =  ['+','-','*','/','%','^']
op1 = ['+','-']
op2 = ['*','/','%']
op3 = ['^']
#-------------------------------------------------------------------------------




# To PRINT STATUS OF STACK AFTER EACH SHIFT AND REDUCE
def show(x):
    print s.string()," "*15,g.displayRev()," "*15,x,"\n"

def end():
    show("REJECT!!")
    exit()

s = Stack()
s.push('$')
exp = str(raw_input("Enter the Expression to check : "))
print "Expression = ",exp
print "STACK"+" "*15+"INPUT"+" "*25 +"OPERATION\n"
g = Stack()
g.push('$')
f=""
# Checking Expression
if exp[0] not in P:
    end()

for i in exp:
    # Reject
    if (i not in P) and (i not in op):
        end()
    if (i not in op):
        f+="P"
    else:
        f+=i

for i in f[::-1]:
    g.push(i)

def Reduce(t):
    s.pop()
    s.push(grammar[t])
    q = "REDUCE "+grammar[t]+"->"+t
    show(q)
    t = s.peek()
    return t

def Reduce2():
    x = s.pop()
    y = s.pop()
    z = s.pop()
    k = z+y+x
    if (k in g1.keys()):
        s.push(g1[k])
        q = "REDUCE "+g1[k]+"->"+k
        show(q)


show("TAKE INPUT")


while (1):

    # top of input stack
    i = g.peek()
    # top if Status Stack
    j = s.peek()

    size = g.size()
    l = s.size()

    # break if only $ remains in input stack
    if (size<=1):
        break

    # if only 1 element in stack
    # and next operator is of precedence 1
    if (l==2 and j!='E' and i in op1):
        j = Reduce(j)
        continue

    # for precedence-2 operators
    if(j in g2.keys()):
        s.pop()
        s.push(g2[j])
        q = "REDUCE "+g2[j]+"->"+j
        show(q)
        continue

    # if next is a 1 precedence operator then reduce
    # p to T
    if (j=="P") and (i in op1):
        while(j!="T"):
            j = Reduce(j)
        # if only 1 element in stack reduce to E
        if(l==2):
            j = s.peek()
            j = Reduce(j)
        continue

    # if next  operator is of precedence 1
    # and stack has 3 elements
    if(l == 4) and (i in op1):
        Reduce2()


    # if top of stack is P
    # and next operator is prec 2 ,then reduce
    if(j == "P") and (i in op2):
        while(j!="T"):
            j = Reduce(j)
        continue

    # if input element is P then push to stack (shift)
    if (i == "P") :
        s.push(g.pop())
        show("SHIFT")
        continue

    # operators with precedence -2
    if (i in op2):

        q=""
        l = g.size()
        # Reject
        if (l<3):
            end()
        s.push(g.pop())
        show("SHIFT")
        x = g.peek()

        # Reject
        if(x != "P"):
            end()

        s.push(g.pop())
        show("SHIFT")

        t = s.peek()
        u = g.peek()
        if (u in op3):
            continue
        if (t=="P"):
            Reduce(t)

        # Reducing exp with prec 2 operators
        x = s.pop()
        y = s.pop()
        z = s.pop()
        q += z+y+x
        s.push(grammar[q])
        q2 ="REDUCE T->T"+y+"F"
        show(q2)
        continue

    # operators with precedence -1
    if (i in op1):
        l = g.size()
        # Reject
        if (l<3):
            end()
        t = s.peek()
        if (t=="P"):
            show("SHIFT")
            # reducing till E
            while(t!='E'):
                t = Reduce(t)

        # shifting
        s.push(g.pop())
        show("SHIFT")
        y = g.peek()
        if(y in op):
            end()
        s.push(g.pop())
        show("SHIFT")
        continue

    # operator with precedence 3
    if (i in op3):
        l1 = g.size()
        if (l1<3):
            end()
        s.push(g.pop())
        show("SHIFT")
        x = g.peek()
        # reject
        if (x!="P"):
            end()
        s.push(g.pop())
        show("SHIFT")
        t = g.peek()
        u = s.peek()
        if (t not in op3):
            if (u != "F"):
                Reduce(u)
            while(1):
                l = s.size()
                if (l<3):
                    break
                x = s.pop()
                y = s.pop()
                # if prec 1 operator encountered break
                if (y in op1):
                    s.push(y)
                    s.push(x)
                    break
                z = s.pop()
                k = z+y+x
                # if prec 2 operators are present in stack
                if (k in g2.keys()):
                    s.push(g2[k])
                    q = "REDUCE "+g2[k]+"->"+k
                # Reducing prec 3 operations
                elif (k in g3.keys()):
                    s.push(g3[k])
                    q = "REDUCE "+g3[k]+"->"+k
                show(q)

# After input is empty only reduction can take place NO shifting
while(1):
    size = s.size()
    t = s.peek()
    if(size>2):
        while(t!="T"):
            t = Reduce(t)

    # only prec1 operations left
    if(size == 4):
        Reduce2()

    size = s.size()
    t = s.peek()
    if(size == 2):
        while(t!="E"):
            t = Reduce(t)

        if (t == "E"):
            show("ACCEPT")
            exit()
        else:
            end()

#5+4%2-9/3+5*2-9*1/2+4*2
