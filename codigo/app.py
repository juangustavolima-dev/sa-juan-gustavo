print("escolha alguma coisa do nosso cardapio:n")


print("1- hamburguer")
print("2-bebidas")
print("3-sobremesas")

cadegoria = int(input("\ndigite sua opcao: "))

if cadegoria == 1:
  print("\n--- HAMBURGERES---")
  print("1- X-Burger R$ 25")
  print("2-X-salada R$ 35")
  print("3-X-bacon R$ 25")
  print("4-X-tudo R$ 25")
  print("5-duplo Burger R$ 38")

escolha = int(input("escolha seu lanche: "))

if escolha == 1:
  nome = "X-Burger"
  preco = 27
elif escolha == 2:
  nome = "X salada"
  preco = 35
elif escolha == 3:
  nome = "X bacon"
  preco = 25
elif escolha ==4:
 nome = "X tudo"
 preco = 25
elif escolha ==5:
 nome = "duplo burger"
 preco = 38


elif cadegoria == 2:
 print("\n--- BEBIDAS---")
 print("1 - coca-cola R$ 12")
 print("2 - guarana R$ 10 ")
 print("3- fanta R$ 8")

 escolha = int(input("escolha sua bebida:"))

 if escolha == 1:
   nome = "coca-cola"
   preco = 12
elif escolha ==2:
   nome = "guarana"
   preco = 10 
elif escolha == 3:
    nome = "fanta"
    preco = 8

elif cadegoria == 3:
    print(" SOBREMESAS")
    print("1 - pudim R$ 7")
    print("2-sorvete R$  4")

    escolha = int(input("escolha sua sobremesa:"))

if escolha == 1:
    nome = "pudim"
    preco = 7
elif escolha == 2:
   nome = "sorvete"
   preco = 4




