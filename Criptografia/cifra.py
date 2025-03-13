import os

pontuacao = [".",",","!","?",";",":","(",")","[","]","{","}","-","_","/","\\","|","@","#","$","%","&","*","^","~","`","<",">","=","+","-","*","/","_"," "]
alfabeto= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
especiais_A = ["á","ã","â","à"]
especiais_E = ["é","ê","è"]
especiais_I = ["í","î","ì"]
especiais_O = ["ó","õ","ô","ò"]
especiais_U = ["ú","ü","ù"]

# Função para calcular a cifra de César
def calc_cifra(chave, msg):
    global pontuacao, alfabeto, especiais_A, especiais_E, especiais_I, especiais_O, especiais_U

    msg = msg.lower() # converte a mensagem para minúsculo

    # substitui os caracteres especiais por caracteres comuns
    for letra in msg:
        if letra =="ç":
            msg = msg.replace(letra, "c")
        elif letra in especiais_A:
            msg = msg.replace(letra, "a")
        elif letra in especiais_E:
            msg = msg.replace(letra,"e")
        elif letra in especiais_I:
            msg = msg.replace(letra,"i")
        elif letra in especiais_O:
            msg = msg.replace(letra,"o")
        elif letra in especiais_U:
            msg = msg.replace(letra,"u")
    cripto = ""
    
    chave = chave %26 # garante que a chave seja um número entre 0 e 25

    for letra in range(len(msg)): # percorre a mensagem
        if msg[letra] in pontuacao: # verifica se o caractere é uma pontuação
            cripto+= msg[letra] # adiciona a pontuação à mensagem criptografada

        elif msg[letra] in alfabeto: # verifica se o caractere é uma letra do alfabeto
            pos= alfabeto.index(msg[letra]) # pega a posição da letra no alfabeto
            if pos + chave > 25: # verifica se a posição da letra mais a chave ultrapassa o limite do alfabeto
                pos = pos - 26 # subtrai 26 da posição para voltar ao início do alfabeto
            pos += chave # adiciona a chave à posição
            cripto+= alfabeto[pos] # adiciona a letra criptografada à mensagem

    return cripto

def calc_cifra_inverse(chave, msg):
    global pontuacao, alfabeto, especiais_A, especiais_E, especiais_I, especiais_O, especiais_U

    msg = msg.lower()

    for letra in msg:
        if letra =="ç":
            msg = msg.replace(letra, "c")
        elif letra in especiais_A:
            msg = msg.replace(letra, "a")
        elif letra in especiais_E:
            msg = msg.replace(letra,"e")
        elif letra in especiais_I:
            msg = msg.replace(letra,"i")
        elif letra in especiais_O:
            msg = msg.replace(letra,"o")
        elif letra in especiais_U:
            msg = msg.replace(letra,"u")
 
    cripto = ""
    chave = chave % 26
    chave = chave %26
    for letra in range(len(msg)):
        if msg[letra] in pontuacao:
            cripto+= msg[letra]
        elif msg[letra] in alfabeto:
            pos= alfabeto.index(msg[letra])
            if pos + chave > 25:
                pos = pos - 26
            pos += chave
            cripto+= alfabeto[pos]

    return cripto           

# Função para encriptar a mensagem
def encript():

    chave = int(input("Chave: ")) 
    msg = str(input("Mensagem: "))
    msg_encript = calc_cifra(chave, msg)

    print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃Mensagem Original: {msg}            
┃Chave: {chave}                         
┃Mensagem Cifrada: {msg_encript}               
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

# Função para decriptar a mensagem
def decript():
    Operador = True
    while Operador:
        os.system('cls')

        msg_encript = ["Afjjv qr xzelr jxppx?","xizbqc amocvlw xmzqwlw otz","mxobj ab cxixo xf pxsfl","Fttf dftbs fi hfouf cpb ent, ub nbmvdp","gfekzeyf gvcf tfuzxf, er dfirc!!!"]
        msg_decript = ["dimmy tu achou massa?","partiu segundo periodo glr","parem de falar ai savio", "esse cesar eh gente boa dms, ta maluco","pontinho pelo codigo, na moral!!!"]
        
        print('\n'.join(f"[{index+1}] {msg}" for index, msg in enumerate(msg_encript)))
        opcao = int(input("Mensagem:"))
        chave = int(input("Chave: "))
        msg = calc_cifra_inverse(chave, msg_encript[opcao-1])
        

        print(f"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃Mensagem Original: {msg_encript[opcao-1]}            
    ┃Chave: {chave}                         
    ┃Mensagem Decifrada: {msg}               
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
        Operador = input("deseja continuar? [s/n]... aperte [x] para fazer o teste automático: ")
        if Operador == "n":
            main()
        elif Operador == "x":
            for chave in range(1,26):
                msg = calc_cifra_inverse(chave, msg_encript[opcao-1])
                if msg in msg_decript:
                    print("Chave encontrada!!!")
                    print(f"Chave {chave}: {msg}")
                    break
                else:
                    print(f"\nChave {chave}: {msg}")
                
            print("a chave não está necessriamente entre 1 e 26")
            input("pressione qualquer tecla para continuar")
        else:
            continue
        
def main():
    opcao = input("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Escolha uma opção        ┃ 
┃  [1] Encriptar                  ┃ 
┃  [2] Decriptar                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
➨ """)
 
    match opcao:
        case '1':
            encript()
        case '2':
            decript()
        case _:
            print("Opção inválida")
            main()
            



main()
