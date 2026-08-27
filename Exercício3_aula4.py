nome = str(input("Qual o seu nome?"))
mes_nascimento = int(input("Qual o mês em que você nasceu? "))
ano_nascimento = int(input("Qual o ano do seu nascimento? "))
mes_atual = int(input("Informe o mês atual. "))
ano_atual = int(input("Informe o ano atual. "))

if mes_atual < mes_nascimento:
    print(f"{nome}, você tem {ano_atual - ano_nascimento -1} anos.")

else:
    print(f"{nome}, você tem {ano_atual - ano_nascimento} anos")