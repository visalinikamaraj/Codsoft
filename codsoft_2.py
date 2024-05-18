print("select the operation you want to perform:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

def addition():
    a=int(input("a:"))
    b=int(input("b:"))
    return a+b

def subraction():
    a=int(input("a:"))
    b=int(input("b:"))
    return a-b

def multiplication():
    a=int(input("a:"))
    b=int(input("b:"))
    return a*b

def division():
    a=int(input("a:"))
    b=int(input("b:"))
    return a/b



while (True):
    operation= int(input("enter the operation:"))


    if operation == 1:
       answer=addition()
       print(answer)
    elif operation == 2:
       answer=subraction()
       print(answer)
    elif operation == 3:
       answer=multiplication()
       print(answer)
    elif operation == 4:
       answer=division()
       print(answer)
    else :
       print("invalid")
       print("please enter a valid opration")


