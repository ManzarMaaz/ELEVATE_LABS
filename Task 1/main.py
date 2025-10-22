class Calculator:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        
    def add(self,a,b):
        self.a = a
        self.b = b
        return a+b

    def subtract(self,a,b):
        self.a = a
        self.b = b
        return a-b

    def mutliply(self,a,b):
        self.a = a
        self.b = b
        return a*b

    def divide(self,a,b):
        self.a = a
        self.b = b
        if b != 0:
            return a/b
        else:
            print('Zero Division Error')

    def square(self,a):
        self.a = a
        self.b = b
        return a**2

    def sqroot(self,a):
        self.a = a
        self.b = b
        return a**0.5

    while True:
        print('Welcome to CalC')
        print('Select the below Operations')
        print('1.Addition')
        print('2.Subtract')
        print('3.Multiplication')
        print('4.Division')
        print('5.Square')
        print('6.Square Root')
        print('7.Exit')
        
        choice = input('Select your Input:')
        
        if choice in ('1','2','3','4','5','6','7'):
            a = float(input('Input First Number :'))
            b = float(input('Input Second Number :'))
            
            if choice == '1':
                print(add(a,b))
                
            elif choice == '2':
                print(subtract(a,b))
                
            elif choice == '3':
                print(mutliply(a,b))
                
            elif choice == '4':
                print(divide(a,b))
                
            elif choice == '5':
                print(square(a))
                
            elif choice == '6':
                print(sqroot(a))
                
        elif choice == '7':
            break
            
        else:
            print('Invalid Input... Try Again')
