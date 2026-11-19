TAXA_ENTREGA = 5

CARDAPIO = {
    "1": {
        "titulo": "HAMBÚRGUERES",
        "itens": {
            "1": ("X-Burger", 25),
            "2": ("X-Salada", 35),
            "3": ("X-Bacon", 25),
            "4": ("X-Tudo", 25),
            "5": ("Duplo Burger", 38),
        },
    },
    "2": {
        "titulo": "BEBIDAS",
        "itens": {
            "1": ("Coca-Cola", 12),
            "2": ("Guaraná", 10),
            "3": ("Fanta", 8),
        },
    },
    "3": { 
        "titulo": "SOBREMESAS",
        "itens": {
            "1": ("Pudim", 7),
            "2": ("Sorvete", 4),
        },
    },
}


def escolher(opcoes, mensagem):
    """Pede uma opção ao usuário até ele digitar uma válida."""
    while True:
        escolha = input(mensagem).strip()
        if escolha in opcoes:
            return escolha
        print("Opção inválida, tente novamente.")


def mostrar_categorias():
    print("\nEscolha alguma coisa do nosso cardápio:\n")
    for codigo, categoria in CARDAPIO.items():
        print(f"{codigo} - {categoria['titulo'].capitalize()}")


def escolher_item():
    mostrar_categorias()
    codigo = escolher(CARDAPIO, "\nDigite sua opção: ")
    categoria = CARDAPIO[codigo]

    print(f"\n--- {categoria['titulo']} ---")
    for cod, (nome, preco) in categoria["itens"].items():
        print(f"{cod} - {nome} R$ {preco:.2f}")

    cod_item = escolher(categoria["itens"], "Escolha seu item: ")
    return categoria["itens"][cod_item]


def main():
    pedido = []

    while True:
        nome, preco = escolher_item()
        pedido.append((nome, preco))
        print(f"✔ {nome} adicionado ao pedido.")

        mais = input("\nDeseja adicionar mais algum item? (s/n): ").strip().lower()
        if mais != "s":
            break

    print("\n=== FINALIZAR PEDIDO ===")
    cliente = input("Digite seu nome: ").strip()
    endereco = input("Digite seu endereço: ").strip()

    subtotal = sum(preco for _, preco in pedido)
    total = subtotal + TAXA_ENTREGA

    print("\n--- RESUMO DO PEDIDO ---")
    print(f"Nome: {cliente}")
    print(f"Endereço: {endereco}")
    print("Itens:")
    for nome, preco in pedido:
        print(f"  - {nome}: R$ {preco:.2f}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Entrega:  R$ {TAXA_ENTREGA:.2f}")
    print(f"Total:    R$ {total:.2f}")

    print("\nPedido recebido, obrigado!")


if __name__ == "__main__":
    main()