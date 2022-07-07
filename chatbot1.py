import os

def escolha(resposta):
    if resposta == 1:
        print(f"Me chamo Thiago Lucas. Tenho 20 anos.{os.linesep}")
    elif resposta == 2:
        print(f"Sou estudande de Análise e desenvolvimento de sistemas, pela Uninter.{os.linesep}")
    elif resposta == 3:
        print(f"Tenho maior intimidade com Python, Javascript e Batch.{os.linesep}")
    elif resposta == 4:
        print(f"Linkedin: https://www.linkedin.com/in/thiago-costa-4909491bb/{os.linesep}")
    else:
        print(f"Opção inválida. Digite 1, 2, 3 ou 4.{os.linesep}")

def start():
    print("Bem-vindo ao chatbot1!")
    nome = input("Qual é o seu nome?\n")
    while True:
        print(f"Em que posso ajudar, {nome}?")
        try:
            resposta = int(input(f"[1] - Quem é você?{os.linesep}[2] - Qual é sua formação?{os.linesep}[3] - Quais linguagens conhece?{os.linesep}[4] - Linkedin.\n"))
        except:
            print("Desculpe, não entendi.")
            continue
        else:
            escolha(resposta)


if  __name__ == "__main__":
    start()