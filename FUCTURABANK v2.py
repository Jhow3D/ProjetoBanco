import os
class ContaCorrente:
    def __init__(self,codconta):
        self.codconta = codconta
        self.nome = {}
        self.__ccorrente = {}
        self.__cpoupanca = {}
        self.__senha = {}
    
    def getccorrente(self):
        return self.__ccorrente
    
    def setccorrente(self):
        self.__ccorrente = {}

    def getcpoupanca(self):
        return self.__cpoupanca

    def setcpoupanca(self):
        self.__cpoupanca = {}

    def getsenha(self):
        return self.__senha

    def setsenha(self,senha):
        self.__senha = {}

    def cadastrar_cliente(self):
        ''''
        Função para cadastrar o cliente.
        '''
        self.nome = input("Digite seu nome: ").upper()
        codconta = int(input("Digite um número de 3 digitos para a conta: ")) 
        senha = int(input("Digite uma senha de 4 digitos: "))
        saldo = float(input("Deposite um valor para ativar a conta: "))
        
        while saldo == 0:
            print("Você precisa depositar um valor para criar a conta!")
            saldo = input("Digite um valor para ativar a conta: ")
        
        print("Deposito efetuado!")
        
        self.nome = {codconta:self.nome}
        self.codconta = codconta
        self.ccorrente = {codconta:saldo}
        self.cpoupanca = {codconta:0}
        self.__senha = {codconta:senha}
        print("A sua conta tem o código {} e o seu saldo atual da conta corrente é {} ".format(codconta,saldo))
    
    def validador(self,codconta):
        '''
        Função para validar a senha
        '''
        s = self.__senha[codconta]
        cont = 0
        while cont <= 3:
            s1 = int(input("Digite sua senha : "))
            if s1 == s: 
                permissão = True
                break
            elif s != self.__senha:
                print("Senha errada.")
                permissão = False
                cont += 1
        return permissão

    def mostrar_dados(self):
        ''''
        Função para mostrar informações da conta corrente do cliente na tela.
        '''
        codconta = int(input("Informe seu codigo da conta: "))
        cc.validador(codconta)
        ('+---------------------+')
        print('DADOS DA CONTA CORRENTE')
        print('|Titular: {}'.format((self.nome.get(codconta))))
        print('|Número da Conta: {}'.format(self.codconta))
        print('|Saldo: R$ {}'.format(self.ccorrente.get(codconta)))
        print('+---------------------+')
        ('+---------------------+')
        print('DADOS DA CONTA CORRENTE')
        print('|Titular: {}'.format((self.nome.get(codconta))))
        print('|Número da Conta: {}'.format(self.codconta))
        print('|Saldo: R$ {}'.format(self.cpoupanca.get(codconta)))
        print('+---------------------+')

    def depositar_cc_corrente(self):
        '''''
        Função para adicionar um valor a conta corrente.
        '''''
        codconta = int(input("Digite o código da sua conta: "))
        cc.validador(codconta)
        valor = float(input('Digite o valor do deposito: '))
        saldo = sum([self.ccorrente[codconta]+float(valor)])
        self.ccorrente[codconta] = saldo
        print("O seu saldo da conta corrente agora é R$ {}".format(self.ccorrente[codconta]))

    def sacar_c_corrente(self):
        '''
        Função para sacar um valor da conta corrente.
        '''
        codconta = int(input("Digite o código da sua conta: "))
        cc.validador(codconta)
        valor = float(input('Digite o valor do saque: '))
        saldo = sum([self.ccorrente[codconta]-float(valor)])
        self.ccorrente[codconta] = saldo
        print("O seu saldo da conta corrente agora é R$ {}".format(self.ccorrente[codconta]))

    def aplicar_poupança(self):
        '''
        Função para aplicar um valor na conta poupança 
        '''     
        codconta = int(input("Digite o código da sua conta: "))
        cc.validador(codconta)
        valor = float(input("Digite o valor da aplicação: "))
        saldo = sum([self.cpoupanca[codconta]+float(valor)])
        self.cpoupanca[codconta] = saldo
        saldo1 = sum([self.ccorrente[codconta]-float(valor)])
        self.ccorrente[codconta] = saldo1
        print("Sua aplicação foi realizada!")

    def resgatar_poupança(self):
        '''
        Função para resgatar um valor na conta poupança 
        '''
        codconta = int(input("Digite o código da sua conta: "))
        cc.validador(codconta)
        valor = float(input("Digite o valor do resgate: "))
        saldo = sum([self.cpoupanca[codconta]-float(valor)])
        self.cpoupanca[codconta] = saldo
        saldo1 = sum([self.ccorrente[codconta]+float(valor)])
        self.ccorrente[codconta] = saldo1
    
class ContaPoupanca:
    def __init__(self,nome):
        super().__init__(self.ccpoupanca,nome)
        self.nome = nome
        self.codconta = {}
        self.ccpoupanca = {}

c = None
cc = ContaCorrente(c)

while True:
    print('='*6)
    print("Bem vindo ao Fuctura Bank")
    print('='*6)
    print("O que você deseja fazer ?")
    print('[0] - Se cadastrar ?')
    print('[1] - Consultar seu saldo ?')
    print('[2] - Fazer um deposito na conta corrente ?')
    print('[3] - Sacar um valor da conta corrente ?')
    print('[4] - Fazer uma aplicação na conta poupança ?')
    print('[5] - Resgatar um valor da conta poupança ?')
   
    op = int(input("Digite a opção: "))
    os.system('cls')
    if op == 0:
        cc.cadastrar_cliente()
    elif op == 1:
        cc.mostrar_dados()
    elif op == 2:
        cc.depositar_cc_corrente()
    elif op == 3:
        cc.sacar_c_corrente()
    elif op == 4:
        cc.aplicar_poupança()
    elif op == 5:
        cc.resgatar_poupança()
    
    print("")
    print("Digite 0 - CONTINUAR | 1 - SAIR")
    if int(input()) == 1:
        break






