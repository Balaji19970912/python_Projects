def add(a,b):
    answer = a+b
    return answer

def sub(a,b):
    answer = a-b
    return answer

def mul(a,b):
    answer = a*b
    return answer

def div(a,b):
    if(a == 0 or b == 0):
        print('Invaid input entered!')
        exit()
    else:
        answer = a / b
        return answer

while(1):
    a = (int)(input("Enter value for number 1 : "))
    b = (int)(input("Enter value for Number 2 : "))
    print('''
    1. Add
    2. Sub
    3. Mul
    4. Div
    5. Exit
    ''')
    choice = (int)(input("Enter your choice : "))
    if(choice == 1):
        print(a,'+',b,'=',add(a,b))
    elif(choice == 2):
        print('a + b =',sub(a,b))
    elif(choice == 3):
        print('a + b =',mul(a,b))
    elif(choice == 4):
        print('a + b =',div(a,b))
    else:
        print('Thank you for using basic calculator!')
        exit()