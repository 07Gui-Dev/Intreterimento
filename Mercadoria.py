print("Seja bem-vindo ao sistema de compras do Mercadinho do bairro!")

print("-----------------------------------------------------------------------------------------------")

print("Aqui você pode adicionar mercadorias ao seu carrinho e ver o total da compra no final.")

Mercadoria = {
    1:  {"nome": "Água", "preço": 2.00
},
    2: {"nome": "Leite", "preço": 4.00},
    3: {"nome": "Coca-Cola Lata 350ml", "preço": 6.00},
    4: {"nome": "Pão", "preço": 3.00},
    5: {"nome": "Arroz", "preço": 4.00},
    6: {"nome": "Feijão", "preço": 5.50}
}

Carrinho = []
print("-----------------------------------------------------------------------------------------------")
def exibir_mercadorias():
    print("Mercadorias disponíveis:")
    for codigo, info in Mercadoria.items():
        print(f"Código: {codigo}, Nome: {info['nome']}, Preço: R${info['preço']:.2f}")
def adicionar_ao_carrinho(codigo):
    if codigo in Mercadoria:
        Carrinho.append(Mercadoria[codigo])
        print(f"{Mercadoria[codigo]['nome']} adicionado ao carrinho.")
    else:
        print("Código inválido. Tente novamente.")
def exibir_carrinho():
    if not Carrinho:
        print("Carrinho vazio.")
        return
    print("Itens no carrinho:")
    total = 0
    for item in Carrinho:
        print(f"Nome: {item['nome']}, Preço: R${item['preço']:.2f}")
        total += item['preço']
    print(f"Total: R${total:.2f}")
def main():
    while True:
        exibir_mercadorias()
        escolha = input("Digite o numero da mercadoria para adicionar ao carrinho. Caso nao tenha encontrado o que procura, digite 'sair' para finalizar: ")
        if escolha.lower() == 'sair':
            break
        try:
            codigo = int(escolha)
            adicionar_ao_carrinho(codigo)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")           
    exibir_carrinho()
    print("-----------------------------------------------------------------------------------------------")
    print("Obrigado por ultilizar o sistema de compras do Mercadinho do bairro! Volte sempre.")
    print("-----------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()