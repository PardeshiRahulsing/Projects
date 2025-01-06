def Factorial(x):#Find the factores of enter the number;
    print("The Factorial number is ",x,"are :")
    for i in range(1,x+1):
        if x % i == 0:
            print(i)
num=int (input("Enter the number"))
Factorial(num)