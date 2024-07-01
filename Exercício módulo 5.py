# Criar uma calculadora

class calculadora():
    def __init__(self): #variaveis globais
        self.op = ""
        self.n1 = 0
        self.result = ""
        self.stop1 = True
        
        #todas as operações que a calculadora faz
        
        print(""" Operações
1 ou + = adição
2 ou - = subtração
3 ou * = mutiplicação
4 ou / = divisão
5 ou // = divisão inteira
6 ou % = resto
7 ou ** = pontencia
0 = parar
""")

    def start(self): #para começar a funcioanr a calculadora
        
        listop = ["1","2","3","4","5","6","7","0","+","-","*","/","//","%","**"]
        
        while self.stop1: #while, porque quero uma calculadora que não pare de calcular
            z = True
            self.number()
            if self.result != "":
                self.operation()
            while z == True: #while, só passa quando digita uma operação valida
                z1 = self.type() 
                if z1 in listop:
                    z = False
                else:
                    print("operação não existe, digite novamente")
                    continue
                
    def number(self): #pergunta um número para o usuário 
        self.n1 = float(input("Digite o número: "))

    def type(self): #pergunta qual a operação desejada pelo usuário
        self.op = input("Digite a operação: ")
        if self.op == str(0):
            self.stop()
        if self.result == "":
            self.result = self.n1
        return self.op

    def operation(self): #condição para saber qual operação fazer com os nuúeros passados
        if self.op == str(1) or self.op == "+":
            self.sum()
        elif self.op == str(2) or self.op == "-":
            self.sub()
        elif self.op == str(3) or self.op == "*":
            self.mut()
        elif self.op == str(4) or self.op == "/":
            self.div()
        elif self.op == str(5) or self.op == "//":
            self.div_int()
        elif self.op == str(6) or self.op == "%":
            self.rest()
        elif self.op == str(7) or self.op == "**":
            self.pont()
        return True
                         
    def sum(self): #função soma
        self.result += self.n1
        self.show_result()
        
    def sub(self): #função subtração
        self.result -= self.n1
        self.show_result()
        
    def mut(self): #função mutiplicação
        self.result *= self.n1
        self.show_result()
        
    def div(self): #função divisão
        self.result /= self.n1
        self.show_result()
        
    def div_int(self): #função divisão inteira
        self.result //= self.n1
        self.show_result()
        
    def rest(self): #função resto
        self.result %= self.n1
        self.show_result()
        
    def pont(self): #potencia
        self.result **= self.n1
        self.show_result()
        
    def show_result(self): #printar o resultado toda vez que houver uma operação
        print("Resultado ",self.result)
    
    def stop(self): #funsão para parar o programa
        x = input("Deseja parar a operação (sim ou não)? ")
        if x.lower() == "sim":
            self.show_result()
            self.stop1=False
        else:
            pass

a = calculadora()
a.start()