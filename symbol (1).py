# PYTHON PROGRAM TO IMPLEMENT SYMBOL TABLE 
"""
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

def is_bin(c):
    
    if c in  op:
    	return True
    else:
    	return False   
    

def is_punct(c):
	p = ['\,','\"','\'',';']
	if c in  p:
    	return True
    else:
    	return False 
 """ 	
    	
f = open("code.txt","r+")
f2 = open("output.txt","a+")
binop = ['+','-','*','/','%']
unop = ['!','++','--']
p = ['\,','\"','\'',';']
keywords = ["int","float","long","short","signed","double"]
b = key = var = integer = fl = op = invalid = punct = []
eq=[]
cnt=0       # for no of ,
for line in f:
	line = line.strip('\n').split(" ")
	for i in line :
		lex = i.strip(",")
		if lex in binop :
			f.write("yukti : @ ")

		if (lex == "="):
			eq.append(lex)
		if lex in keywords and lex not in key:
			key.append(lex)


for i in key:
	print i,

















			
