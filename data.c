/*
PROBLEM STATEMENT :
 int a ;
 int b,c ;
 c = a + b ;
 1. verify if all the variables have a valid datatype (int,float,long,double,short,char)
 2. verify if variables in an expression have the same datatype

*/

/* Limitation :
Code works to check variable only of length 1
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	
	int i,n,j,k,l,x=0,y=0,z,pos,n2,vc=0,m;   // vc = variable count
	char code[100];            // declared a character array for string space separated codeline as input
	
	int type[100];     
	char variable[100];       // to store variable names
	char exp[100];            // for expression
	printf("Enter the number of declarative statements in the code = ");
	scanf("%d\n",&n);        // '\n' impotant otherwise gets take newline char as input in 1st iteration
	for(i=0; i<n; i++){	
		char datatype[20];         // to store datatypes	
		gets(code);  
		l = strlen(code);
		if (code[l-1] != ';'){
			printf("Syntax Error!! Aborting....\n");
			exit(0);
		}
		k=0;
		for(j=0;j<l;j++){
			if (code[j] == ' '){
				pos = j;
				break;
			}				
			datatype[k++] = code[j];
				
		}
		for(m=pos+1;m<l;m++){
			if (code[m]>=97 && code[m]<=122){
				if (strchr(variable,code[m])==NULL)
					variable[vc++] = code[m];
				else{
					printf("%c is already declared! Aborting...\n",code[m]);
					exit(0);
				}
			}
		}
		
		if (strcmp(datatype,"int")==0){
			while(x!=vc){
				type[x++] = 1;
			}
		}			
		else if (strcmp(datatype,"float")==0){
			while(x!=vc){
				type[x++] = 2;
			}
		}
		else if (strcmp(datatype,"long")==0){
			while(x!=vc){
				type[x++] = 3;
			}
		}
		else if (strcmp(datatype,"double")==0){
			while(x!=vc){
				type[x++] = 4;
			}
		}
		else if (strcmp(datatype,"char")==0){
			while(x!=vc){
				type[x++] = 5;
			}
		}
		else if (strcmp(datatype,"short")==0){
			while(x!=vc){
				type[x++] = 6;
			}
		}
		else{
			printf("Invalid Datatype!! Aborting...\n");
			exit(0);
		}
		memset(datatype, 0, sizeof(datatype));   // to clear/reset the char array after each iteration	
	}
	printf("Enter the number of expressions = ");
	scanf("%d\n",&n2);
	int a;
	for(a=0;a<n2;a++){		
		gets(exp); 
		//printf("\n%s\n",exp);
		int l2 = strlen(exp),f=0,I=0,F=0,L=0,D=0,C=0,S=0,c=0;
		if (exp[l2-1] != ';'){
			printf("Invalid Syntax! Aborting....");
			exit(0);
		}
		char ch;
		f=0;
		for(i=0; i<l2; i++){
			
			if (exp[i]>=97 && exp[i]<=122){
				c++;
				ch = exp[i];
				for(j=0;j<x;j++){
					if (ch == variable[j]){
						f = type[j];
						if (f == 1) I++;
						else if (f==2) F++;
						else if (f==3) L++;
						else if (f==4) D++;
						else if (f==5) C++;
						else if (f==6) S++;	
						else{
							printf("Undeclared Variable! Aborting....\n");
							exit(0);							
						}				
						
					}
				}
			}
		}
		if (I==c || F==c || L==c || D==c || C==c || S==c  )
			printf("VALID DATATYPE!\n");
		else
			printf("INVALID!! DATATYPE MISMATCH!\n");
	}
	return 0;
}
