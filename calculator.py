
print("1 - Add")
print("2 - Substract")
print("3 - Multiply")
print("4 - Division")
option=int(input("choose an operation:"))
result=0

if(option in[1,2,3,4]):
    n1=float(input("enter first number:"))
    n2=float(input("enter second number:"))

    if(option==1):
        result=n1+n2
    elif(option==2):
        result=n1-n2
    elif(option==3):
        result=n1*n2
    elif(option==4):
        result=n1 / n2



else:
    print("invalid operation entered")
print("the result of the operation is:{}".format(result))