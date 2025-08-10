import numpy as np 

hist=[]
# print(hist.)
x=input('enter one: s for Start ,e for End ,h for history :\n  ') 
while(True):
    if x =='s' or x=='c':
        a=int(input("enter ur first number : ", ))
        b=input("calculation :")
        r=int(input(' second number : ', ))
        ch=0
        if b=="sum " or b=='+' :
            # d=a+r
            hist.append(a+r)
            print('ersult is :', a+r)
            ch+=1
        elif b=='minus' or b=='-' :
            d=a-r 
            hist.append(d)
            print('result is :', d)
            ch+=1
        elif b=='multiply' or b=='*' :
            d=a*r
            hist.append(d)
            print('result is :', d)
            ch+=1
        elif b=='divide' or b=='/' :
            d=a/r
            hist.append(d)
            print('result is :', d) 
            ch+=1
        else :
            print('out of range')
    elif x=="h":
        if hist:
            print(hist)
        else :
            print("no previous history")
    elif x=="ch":
        i=0
        while(i < ch):
            hist.pop()
            i+=1                  
    elif x=='e':
        break;
    else :
        print('invalid literal ! Try again ')
    x=input('enter one: c to continue ,e for End ,h for history ' ) 
           
