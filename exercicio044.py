print("Administrando Pagamentos!")

preco = float(input("Qual o preço do produto? R$"))

forma_pagamento = int(input("Qual a forma de pagamento? \n[1] À Vista dinheiro/cheque \n[2] À Vista no Cartão "
                            "\n[3] 2x no Cartão \n[4] 3x ou mais no Cartão \nSua Opção: "))

if forma_pagamento == 1:
    desconto = preco * (10 / 100)
    preco = preco - desconto
    print(f"Pagando à vista com dinheiro você receberá um desconto de 10% (R${desconto:.2f})")
    print(f"O preço final do produto será de R${preco:.2f}")
elif forma_pagamento == 2:
    desconto = preco * (5 / 100)
    preco = preco - desconto
    print(f"Pagando à vista com cartão você receberá um desconto de 5% (R${desconto:.2f})")
    print(f"O preço final do produto será de R${preco:.2f}")
elif forma_pagamento == 3:
    print("Pagando no cartão em 2x você não terá juros, mas não conta com descontos.")
    print(f"O preço final do produto será de R${preco:.2f}")
elif forma_pagamento == 4:
    qtd_parcelas = int(input("Quantas parcelas: "))
    juros = preco * (20 / 100)
    preco = preco + juros
    preco_parcela = preco / qtd_parcelas
    print(f"Pagando no cartão em {qtd_parcelas}x você pagará uma taxa de juros de 20% (R%{juros:.2f})")
    print(F"Cada parcela sairá por R${preco_parcela}")
    print(f"O preço final do produto será de R${preco:.2f}")
else:
    print("Opção Inválida! Tente rodar o programa novamente!")