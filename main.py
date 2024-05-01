poltrona1Identificador = 1
poltrona1NomeDoLocador = ''
poltrona1Disponibilidade = True

poltrona2Identificador = 2
poltrona2NomeDoLocador = ''
poltrona2Disponibilidade = True

poltrona3Identificador = 3
poltrona3NomeDoLocador = ''
poltrona3Disponibilidade = True

poltrona4Identificador = 4
poltrona4NomeDoLocador = ''
poltrona4Disponibilidade = True

poltrona5Identificador = 5
poltrona5NomeDoLocador = ''
poltrona5Disponibilidade = True

numeroEscolhido = 10
numeroPoltronaEscolhida = 0
nomeLocadorPoltrona = ""

def verificaDisponibilidadePoltronaEspecifica(numeroPoltrona):
    if(numeroPoltrona == 1):
        return poltrona1Disponibilidade
    if(numeroPoltrona == 2):
        return poltrona2Disponibilidade
    if(numeroPoltrona == 3):
        return poltrona3Disponibilidade
    if(numeroPoltrona == 4):
        return poltrona4Disponibilidade
    if(numeroPoltrona == 5):
        return poltrona5Disponibilidade
    

def verificaDisponibilidadePoltronas():
    if((poltrona1Disponibilidade == False) and (poltrona2Disponibilidade == False) and (poltrona3Disponibilidade == False) and (poltrona4Disponibilidade == False) and (poltrona5Disponibilidade == False)):
        return False
    return True

def listaPoltronasDisponiveis():
    if(verificaDisponibilidadePoltronas() == False):
        print("Teatro lotado. Todas as poltronas estão ocupadas!")
        return
    
    if(poltrona1Disponibilidade == True):
        print("Poltrona 1 está disponível")
    if(poltrona1Disponibilidade == False):
        print("Poltrona 1 está indisponível")

    if(poltrona2Disponibilidade == True):
        print("Poltrona 2 está disponível")
    if(poltrona2Disponibilidade == False):
        print("Poltrona 2 está indisponível")

    if(poltrona3Disponibilidade == True):
        print("Poltrona 3 está disponível")
    if(poltrona3Disponibilidade == False):
        print("Poltrona 3 está indisponível")

    if(poltrona4Disponibilidade == True):
        print("Poltrona 4 está disponível")
    if(poltrona4Disponibilidade == False):
        print("Poltrona 4 está indisponível")  

    if(poltrona5Disponibilidade == True):
        print("Poltrona 5 está disponível")    
    if(poltrona5Disponibilidade == False):
        print("Poltrona 5 está indisponível")               

def reservarPoltrona():
    listaPoltronasDisponiveis()
    print("--------------------------------------")
    print("Digite o número da poltrona que deseha reservar!")
    numeroPoltronaEscolhida = int(input())

    while ((numeroPoltronaEscolhida < 1) or (numeroPoltronaEscolhida > 5) or (verificaDisponibilidadePoltronaEspecifica(numeroPoltronaEscolhida) == False)):
        if(verificaDisponibilidadePoltronaEspecifica(numeroPoltronaEscolhida) == False):
            print("Esta poltrona está ocupada, escolha outra!")
        else:    
            print("Digite o número de uma poltrona existente!")
        numeroPoltronaEscolhida = int(input())

    print("Digite o nome do locador da poltrona!")
    nomeLocadorPoltrona = str(input())

    print(numeroPoltronaEscolhida)

    match numeroPoltronaEscolhida:
        case 1:
            global poltrona1Disponibilidade
            global poltrona1NomeDoLocador
            poltrona1Disponibilidade = False
            poltrona1NomeDoLocador = nomeLocadorPoltrona
        case 2:
            global poltrona2Disponibilidade
            global poltrona2NomeDoLocador
            poltrona2Disponibilidade = False
            poltrona2NomeDoLocador = nomeLocadorPoltrona
        case 3:
            global poltrona3Disponibilidade
            global poltrona3NomeDoLocador
            poltrona3Disponibilidade = False
            poltrona3NomeDoLocador = nomeLocadorPoltrona
        case 4:
            global poltrona4Disponibilidade
            global poltrona4NomeDoLocador
            poltrona4Disponibilidade = False
            poltrona4NomeDoLocador = nomeLocadorPoltrona
        case 5:
            global poltrona5Disponibilidade
            global poltrona5NomeDoLocador
            poltrona5Disponibilidade = False
            poltrona5NomeDoLocador = nomeLocadorPoltrona   

    print("A poltrona " + str(numeroPoltronaEscolhida) + " foi reservada por " + str(nomeLocadorPoltrona))     
               
def cancelarReservaPoltrona():
    print("Digite o número da poltrona que deseja reservar!")
    numeroPoltronaEscolhida = int(input())
    
    while ((numeroPoltronaEscolhida < 1) or (numeroPoltronaEscolhida > 5) or (verificaDisponibilidadePoltronaEspecifica(numeroPoltronaEscolhida) == True)):
        if(verificaDisponibilidadePoltronaEspecifica(numeroPoltronaEscolhida) == True):
            print("Esta poltrona está disponível, escolha outra!")
        else:    
            print("Digite o número de uma poltrona existente!")
        numeroPoltronaEscolhida = int(input())
    
    match numeroPoltronaEscolhida:
        case 1:
            global poltrona1Disponibilidade
            global poltrona1NomeDoLocador
            poltrona1Disponibilidade = True
            poltrona1NomeDoLocador = ""
        case 2:
            global poltrona2Disponibilidade
            global poltrona2NomeDoLocador
            poltrona2Disponibilidade = True
            poltrona2NomeDoLocador =  ""
        case 3:
            global poltrona3Disponibilidade
            global poltrona3NomeDoLocador
            poltrona3Disponibilidade = True
            poltrona3NomeDoLocador = ""
        case 4:
            global poltrona4Disponibilidade
            global poltrona4NomeDoLocador
            poltrona4Disponibilidade = True
            poltrona4NomeDoLocador = ""
        case 5:
            global poltrona5Disponibilidade
            global poltrona5NomeDoLocador
            poltrona5Disponibilidade = True
            poltrona5NomeDoLocador = ""
    print("A reserva da poltrona " + str(numeroPoltronaEscolhida) + " foi cancelada com sucesso!")      

    
def consultarPoltornaPorNumero():
    print("Digite o numero da poltrona que deseja consultar!")
    numeroEscolhido = int(input())
    while (numeroEscolhido < 1 or numeroEscolhido > 5):
        print("Digite o número de uma poltrona existente!")
        numeroEscolhido = int(input())

    match numeroEscolhido:
        case 1:
            if poltrona1Disponibilidade == False:
                print("A poltrona 1 está ocupada por " + str(poltrona1NomeDoLocador))
                return
            print("A poltrona 1 está disponível")
            return
        case 2:
            if poltrona2Disponibilidade == False:
                print("A poltrona 2 está ocupada por " + str(poltrona2NomeDoLocador))
                return
            print("A poltrona 2 está disponível")
            return
        case 3:
            if poltrona3Disponibilidade == False:
                print("A poltrona 3 está ocupada por " + str(poltrona3NomeDoLocador))
                return
            print("A poltrona 3 está disponível")
            return       
        case 4:
            if poltrona4Disponibilidade == False:
                print("A poltrona 4 está ocupada por " + str(poltrona4NomeDoLocador))
                return
            print("A poltrona 4 está disponível")
            return  
        case 5:
            if poltrona5Disponibilidade == False:
                print("A poltrona 5 está ocupada por " + str(poltrona5NomeDoLocador))
                return
            print("A poltrona 5 está disponível")
            return


while numeroEscolhido != 0:
    print("--------------------------------------")
    print("--------------------------------------")
    print("1 - POLTRONAS DISPONIVEIS")
    print("2 - RESERVAR POLTRONA")
    print("3 - CANCELAR RESERVA")
    print("4 - CONSULTAR POLTRONA ESPECIFICA")
    print("0 - ENCERRAR")

    numeroEscolhido = int(input())  

    match numeroEscolhido:
        case 1:
            listaPoltronasDisponiveis()
        case 2:
            reservarPoltrona()    
        case 3:
            cancelarReservaPoltrona() 
        case 4:
            consultarPoltornaPorNumero()       
        case 0:
            print("Encerrando consulta, tenha um ótimo dia!")
        case _:
            print("Digite uma opção valida!")       

