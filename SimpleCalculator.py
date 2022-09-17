def makecount(num1,num2,x):
    match x:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            return num1/num2
        case _:
            return 0   # 0 is the default case if x is not found

fullcount=input("Please enter the count:")

operators = ["-","+","*","/"]
for x in operators:
    num = fullcount.find(x)
    if num != -1:
        operator = fullcount[num]
        
numbers = fullcount.split(operator)
number1=float(numbers[0])
number2=float(numbers[1])
result = makecount(number1,number2,operator) 
if result == 0: 
    print("Operator not suported!")
else:
    print(result)