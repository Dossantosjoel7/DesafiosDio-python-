
#Cadastrar usuario(criar um cliente)  e cadastrar conta bancaria(criar conta corrente(vincular com usuario)
#modularizar sacar, depositar e visualizar extrato

#saque - por keyword only , sugestão argumentos: saldo,valor, extrato,limite,numero_saques,limite_saques - sugestão de retorno :saldo  e extrato
#deposito - por positional only, sugestaõ de arg: saldo,valor,extrato. sugestão de ret: saldo e extrato
#extrato - por dois, arg posicional saldo e arg nomeados: extrato
#tens liberdade de criar novas funções listar contas

#
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuario = []
conta = []


"""
def ChecagemCpf():
    cpf = input("Digite o cpf -> ")
    while((len(cpf)) != 11 and (len(cpf)) != 14 ):
        print("Deve ser 11 números")v
        cpf = input("Digite o cpf -> ")
        
    if((len(cpf)) == 11):
        return int(cpf)
    else:
        cpf_semcaracteres = "".join([char for char in cpf if char !="-" and char !="."])
        return int(cpf_semcaracteres)
"""

def ChecagemCpf():
    while(True):
        cpf = input("Digite o cpf -> ")
        cpf_semcaracteres = "".join([char for char in cpf if char.isdigit()])
        
        if((len(cpf_semcaracteres)) == 11 and cpf_semcaracteres.isdigit() ):
            return cpf_semcaracteres
        else:
            print("CPF inválido! Digite apenas os 11 dígitos do CPF (com ou sem formatação).")
    
def VerificarCpf(cpf,usuario):
    x = 0
    for i in usuario:
        if(i["cpf"] == cpf):
            x = 1
            break
        else:
            x = 0
    return x
    

def CriarUsuario(usuario):
    nome = input("Declare o nome -> ")
    while True:
        data_nascimento = input("Digite a data do Nascimento[DD/MM/YYYY] -> ")
        pats = data_nascimento.split("/")
        
        if len(pats) != 3 or not (pats[0].isdigit() and pats[1].isdigit() and pats[2].isdigit()):
            print("Formato inválido! Use DD/MM/AAAA e apenas números.")
            continue

        dia = int(pats[0])
        mes = int(pats[1])
        ano = int(pats[2])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1900 or ano > 2025:
            print("Data inválida! Verifique os valores de dia, mês e ano.")
            continue
        
        if(len(pats) != 3 and  data_nascimento.isalpha()):
            print("Formato inválido! Use DD/MM/AAAA.")
            continue
        else:
            break
   
    while True:
        user = 0
        cpf = ChecagemCpf()
        if ((VerificarCpf(cpf,usuario)) == 0):
            print("Declare o Endereço -> \n")
            logradouro = input("logradouro -> ")
            numero = input("número -> ")
            bairro = input("bairro -> ")
            cidade = input("cidade -> ")
            estado = input("estado -> ")
            endereco = {"logradouro":logradouro,"numero":numero,"bairro":bairro,"cidade":cidade,"estado":estado}
            user = {"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco}
            usuario.append(user)
            user = 1
            break
        else:
            print("Existe CPF igual no Sistema")
            continue
    return user


def CriarConta(conta, usuario):
    while True:
        cpf = ChecagemCpf()

        # Verificar se o usuário existe
        user_exists = VerificarCpf(cpf, usuario)
        if user_exists == 0:
            print("Não existe usuário no sistema com este CPF.")
            continue

        # Encontrar o usuário associado ao CPF
        user = None
        for u in usuario:
            if u["cpf"] == cpf:
                user = u
                break

        # Encontrar o maior número de conta já criado
        max_num_conta = 0
        for c in conta:
            if c["num_conta"] > max_num_conta:
                max_num_conta = c["num_conta"]

        # Criar o número da nova conta
        num_conta = max_num_conta + 1

        # Criar a nova conta
        nova_conta = {
            "agencia": "0001",
            "num_conta": num_conta,
            "user": user
        }

        # Adicionar a nova conta à lista de contas
        conta.append(nova_conta)
        print(f"Conta criada com sucesso! Número da conta: {num_conta}")
        break


def Deposito(saldo,extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def Saque(*,saldo,extrato,numero_saques,limite):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
       print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
       print("Operação falhou! Número máximo de saques excedido.")
       
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def Extrato(saldo,/,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def Menu():
    
    menu = """

    [u] Cadastrar Usuario
    [v] Criar Conta Vinculada
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return menu
    
# Main

    
while True:
    
    opcao = input(Menu())

    if opcao == "d":
        saldo,extrato = Deposito(saldo,extrato)
    elif opcao == "u":
        CriarUsuario(usuario)
        print(usuario)
    elif opcao == "v":
        CriarConta(conta,usuario)
        print(conta)
    elif opcao == "s":
        saldo,extrato,numero_saques = Saque(saldo=saldo,extrato=extrato,numero_saques=numero_saques,limite = limite)
    elif opcao == "e":
        Extrato(saldo, extrato=extrato)
    elif opcao == "q":
       break
    else:
        print("Operação invdálida, por favor selecione novamente a operação desejada.")