#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yukti
#
# Created:     02-09-2018
# Copyright:   (c) yukti 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import re


def is_ident(s):
    s.strip(",")
    if (s not in keywords):
        pattern = r"^[_a-zA-Z][_a-zA-Z0-9]*$"
        if re.match(pattern,s):
            return 1
        else:
            return 0


keywords = ["int","float","long","char","string","unsigned","short","return","break","continue","static","if","for","while","case","static","void","extern","enum","else","sizeof","goto"]       # @
b_op = ['+','-','*','/','%','&&','||','>','<']        # $
punct = ['!',';','[',']','{','}','#','//','/*','*/','(',')',',','>','<']
assig = ['=','+=','/=','-=','*=','%=']           #&


ident = []
b=[]
c=0
v=0
f = open("code.txt","r");
f2 = open("symbol.txt",'w+')
f2.write("*****************************THE SYMBOL TABLE*****************************\n\n")
f2.write("\tkeywords\t:\t@\n")
f2.write("\tIdentifiers\t:\t!\n")
f2.write("\tBinary Op\t:\t$\n")
f2.write("\tAssignment\t:\t&\n")
f2.write("\tPunctuation\t:\t%\n\n\n")
n=[]



for line in f :
    # the  C-compiler ignores what's inside the strings
    if (re.findall('"([^"]*)"', line)):
        continue
    line = line.strip("\n").split(" ")

    # checking for commented lines
    if (line[0] in ['//']):
        if('//' not in n):
            n.append(line[0])
            c+=1
            f2.write(str(c)+ ".\t"+ line[0] + "\t:\t%\n")
        continue

    # header files
    if ('#' in line[0] and '#' not in n) :
        c+=1
        n.append('#')
        f2.write(str(c)+ ".\t"+ '#' + "\t:\t%\n")
        continue

    for word in line:

        #checking for keywords
        if (word in keywords and word not in n):
            n.append(word)
            c+=1
            f2.write(str(c)+".\t"+word+"\t:\t@\n" )


        if (word in b_op and word not in b):
                n.append(word)
                b.append(word)
                c+=1
                f2.write(str(c)+".\t"+ word + "\t:\t$\n")

        if (word in assig and word not in n):
            n.append(word)
            c+=1
            f2.write(str(c)+".\t"+ word + "\t:\t&\n")

        for x in word:

            #checking for punctuations
            if (x in punct and x not in n):
                n.append(x)
                c+=1
                f2.write(str(c)+ ".\t"+ x + "\t:\t%\n")

            #checking for binary operators
            elif (x in b_op and x not in b):
                n.append(x)
                b.append(x)
                c+=1
                f2.write(str(c)+".\t"+ x + "\t:\t$\n")

            #checking for assignment operators
            elif (x in assig and x not in n):
                n.append(x)
                c+=1
                f2.write(str(c)+".\t"+ x + "\t:\t&\n")

        # checking for identifiers
        word = word.strip(",")
        if(word):
            if (word not in n and is_ident(word)):
                n.append(word)
                ident.append(word)
                c+=1
                f2.write(str(c)+ ".\t"+ word + "\t:\t!\n")
f2.close()
f.close()

# To print the contents of output file
fout = open("symbol.txt","r")
for i in fout:
    print i,
fout.close()

