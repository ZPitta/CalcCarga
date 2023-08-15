import math
from time import sleep
import os

produtos = {
    '060': {
        'Descrição': 'Goiabada Ramy Fl 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 316.0
        },
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto': 7.36
        },
        'Paletização': {
            'N CX Camada': 13,
            'N Camada Pallet': 9,
            'N CX Pallet': 117
        }
    },
    '362': {
        'Descrição': 'Amido de Milho Ramy 200g',
        'Validade': 18,
        'Unidade': {
            'Peso Bruto g/kg': 224.0
        },
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto': 5.0
        },
        'Paletização': {
            'N CX Camada': 13,
            'N Camada Pallet': 8,
            'N CX Pallet': 104
        }
    },
    '785': {
        'Descrição': 'Ketchup Ramy Trad. Frs 400g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 435.9
        },
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto': 10.48
        },
        'Paletização': {
            'N CX Camada': 11,
            'N Camada Pallet': 6,
            'N CX Pallet': 66
        }
    },
    '581': {
        'Descrição': 'Molho de Tomate Peneirado Ramy Sachê 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 306.0
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '787': {
        'Descrição': 'Mostarda Ramy Frs 190g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 209.0
        },
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto': 5.23
        },
        'Paletização': {
            'N CX Camada': 15,
            'N Camada Pallet': 7,
            'N CX Pallet': 105
        }
    },
    '790': {
        'Descrição': 'Molho Mostarda Ramy Sachê Bico 180g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 185.0
        },
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto': 5.92
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '571': {
        'Descrição': 'Maionese Tradicional Ramy Sachê Bico 180g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 185.0
        },
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto': 5.92
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '789': {
        'Descrição': 'Ketchup de Tomate Trad. Ramy Sachê Bico 180g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 185.0
        },
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto': 5.92
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '788': {
        'Descrição': 'Ketchup de Tomate Ramy Sachê Bico 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 305.0
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.42
        },
        'Paletização': {
            'N CX Camada': 15,
            'N Camada Pallet': 6,
            'N CX Pallet': 90
        }
    },
    '791': {
        'Descrição': 'Molho Barbecue Ramy Sachê Bico 180g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 185.0
        },
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto': 5.92
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '580': {
        'Descrição': 'Molho de Tomate Trad. Ramy Sachê 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 306
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '582': {
        'Descrição': 'Extrato de Tomate Ramy Sachê 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 306
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '587': {
        'Descrição': 'Molho de Tomate Manjericão Ramy Sachê 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 306.0
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '588': {
        'Descrição': 'Molho de Tomate Pizza Ramy Sachê Bico 180g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 306.0
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '589': {
        'Descrição': 'Molho de Tomate Ervas Finas Ramy Sachê 300g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 306.0
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '690': {
        'Descrição': 'Molho de Tomate Trad. Ramy Sachê 1,7 Kg',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 1.73
        },
        'Cx Embarque': {
            'Quantidade': 6,
            'Peso Bruto': 10.88
        },
        'Paletização': {
            'N CX Camada': 10,
            'N Camada Pallet': 7,
            'N CX Pallet': 70
        }
    },
    '792': {
        'Descrição': 'Milho Sachê Ramy 1,7 Kg',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 1.73
        },
        'Cx Embarque': {
            'Quantidade': 6,
            'Peso Bruto': 10.88
        },
        'Paletização': {
            'N CX Camada': 7,
            'N Camada Pallet': 6,
            'N CX Pallet': 42
        }
    },
    '141': {
        'Descrição': 'Maionese Tradicional Ramy Mini Sachê 7g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 7.0089
        },
        'Cx Embarque': {
            'Quantidade': 144,
            'Peso Bruto': 1.05
        },
        'Paletização': {
            'N CX Camada': 36,
            'N Camada Pallet': 11,
            'N CX Pallet': 396
        }
    },
    '140': {
        'Descrição': 'Ketchup Tradicional Ramy Mini Sachê 7g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 7.0089
        },
        'Cx Embarque': {
            'Quantidade': 144,
            'Peso Bruto': 1.05
        },
        'Paletização': {
            'N CX Camada': 36,
            'N Camada Pallet': 11,
            'N CX Pallet': 396
        }
    },
    '142': {
        'Descrição': 'Mostarda Ramy Mini Sachê 7g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 7.0089
        },
        'Cx Embarque': {
            'Quantidade': 144,
            'Peso Bruto': 1.05
        },
        'Paletização': {
            'N CX Camada': 36,
            'N Camada Pallet': 11,
            'N CX Pallet': 396
        }
    },
    '886': {
        'Descrição': 'Milho Crocante ao Vapor Ramy Lt 170g',
        'Validade': 30,
        'Unidade': {
            'Peso Bruto g/kg': 270.2
        },
        'Cx Embarque': {
            'Quantidade': 30,
            'Peso Bruto': 7.15
        },
        'Paletização': {
            'N CX Camada': 6,
            'N Camada Pallet': 18,
            'N CX Pallet': 108
        }
    },
    '887': {
        'Descrição': 'Ervilha Crocante ao Vapor Ramy Lt 170g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 236.8
        },
        'Cx Embarque': {
            'Quantidade': 30,
            'Peso Bruto': 7.15
        },
        'Paletização': {
            'N CX Camada': 6,
            'N Camada Pallet': 18,
            'N CX Pallet': 108
        }
    },
    '888': {
        'Descrição': 'Dueto Crocante ao Vapor Ramy 170g',
        'Validade': 12,
        'Unidade': {
            'Peso Bruto g/kg': 236.8
        },
        'Cx Embarque': {
            'Quantidade': 30,
            'Peso Bruto': 7.15
        },
        'Paletização': {
            'N CX Camada': 6,
            'N Camada Pallet': 11,
            'N CX Pallet': 108
        }
    },
    '882': {
        'Descrição': 'Milho Verde em Conserva Ramy Sachê 170g',
        'Validade': 30,
        'Unidade': {
            'Peso Bruto g/kg': 270.2
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '883': {
        'Descrição': 'Dueto em Conserva Ramy Sachê 170g',
        'Validade': 30,
        'Unidade': {
            'Peso Bruto g/kg': 270.2
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '884': {
        'Descrição': 'Ervilha em Conserva Ramy Sachê 170g',
        'Validade': 30,
        'Unidade': {
            'Peso Bruto g/kg': 270.2
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '885': {
        'Descrição': 'Seleta de Legumes em Conserva Ramy Sachê 170g',
        'Validade': 30,
        'Unidade': {
            'Peso Bruto g/kg': 270.2
        },
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '890': {
        'Descrição': 'Azeite de Oliva Extra Virgem Ramy Gf 500ml',
        'Validade': 24,
        'Unidade': {
            'Peso Bruto g/kg': 826.0
        },
        'Cx Embarque': {
            'Quantidade': 12,
            'Peso Bruto': 10.37
        },
        'Paletização': {
            'N CX Camada': 26,
            'N Camada Pallet': 5,
            'N CX Pallet': 130
        }
    }
}


def limpa_tela():  # Função utilizada para limpar a tela do usuário
    os.system('cls' if os.name == 'nt' else 'clear')


def main():  # Função principal, utilizada para iniciar o programa
    while True:
        while True:
            try:
                print("""Opções disponíveis:

                1 - Obter Peso total em Kg, quantidade de caixas e pallets.
                2 - Ver todos os itens cadastrados.
                3 - Em construção.

                9 - Encerra o programa.""")

                opcao = int(input("\nSelecione a opção desejada: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
                sleep(2)
                limpa_tela()
        if opcao == 3 or opcao == 2 or opcao == 1 or opcao == 9:
            menu(opcao)
        else:
            print("Entrada inválida. Digite um número válido.")
            sleep(2)
            limpa_tela()


def menu(opcao):  # Função utilizada para acessar o menu e definir o próximo passo do programa
    match opcao:
        case 1:
            calc_peso_vol()
        case 2:
            relatorio_prods()
        case 3:
            print("Você selecionou: 3 - Em construção.")
            sleep(1)
            print("Função em construção, favor aguardar.")
            sleep(3)
            limpa_tela()
            main()
        case 9:
            print("Obrigado por utilizar o programa.")
            sleep(1)
            exit()


def calc_peso_vol():  # Função utilizada para calcular o peso total do pedido em kg, volume e quantidade de pallets
    print("Você selecionou: 1 - Obter Peso total em Kg, quantidade de caixas e pallets.")
    sleep(1)
    qtd_itens = int(input("\nInforme a quantidade de itens/produtos no total: "))
    soma = 0
    volume = 0
    contz = 0
    for cont in range(0, qtd_itens):
        while contz < qtd_itens:
            prod = str(input("\nInforme os três ultímos digitos do código do produto desejado: "))
            achou = False
            for chave in produtos:
                if prod == chave:
                    achou = True
                    qtd_cx = int(input("\nInforme a quantidade de caixas do produto {0}: "
                                       .format(produtos[chave]['Descrição'])))
                    soma = soma + (qtd_cx * produtos[chave]['Cx Embarque']['Peso Bruto'])
                    volume = volume + qtd_cx
                    print("\n{0}".format("-*-" * 32))
                    contz += 1
            if not achou:
                print("\nProduto não encontrado. Tente novamente")
                sleep(1)
    limpa_tela()
    qtd_pallets = math.ceil(volume / 96)
    peso_final = soma + (qtd_pallets * 30)
    print("\n{0}\n".format("-*-" * 32))
    print("Peso total da carga: {0:.2f} Kg".format(soma))
    print("Volume total da carga: {0} caixas".format(volume))
    print("Quantidade total de pallets da carga: {0}".format(qtd_pallets))
    print("Peso total da carga com os pallets: {0:.2f} Kg".format(peso_final))
    print("\n{0}\n".format("-*-" * 32))
    print("Em 5 segundos você poderá escolher novamente outra função.")
    sleep(5)
    main()


def relatorio_prods():  # Função utilizada para listar todos os produtos presentes no dicionário 'produtos'
    print("Você selecionou: 2 - Ver todos os itens cadastrados.")
    sleep(1)
    print("Vou te mostrar os produtos cadastrados.")
    sleep(1)
    for codigo, detalhes in produtos.items():
        print('-=' * 80)
        print(f"Código do produto: {codigo}\n")
        print(f"Descrição: {detalhes['Descrição']}")
        print(f"Validade: {detalhes['Validade']} meses")
        print(f"Unidade - Peso Bruto: {detalhes['Unidade']['Peso Bruto g/kg']:.2f} kg")
        print(f"Cx Embarque - Quantidade: {detalhes['Cx Embarque']['Quantidade']}")
        print(f"Cx Embarque - Peso Bruto: {detalhes['Cx Embarque']['Peso Bruto']:.2f} kg")
        print(f"Paletização - N° Cx p/ Camada: {detalhes['Paletização']['N CX Camada']}")
        print(f"Paletização - N° Camada p/ Pallet: {detalhes['Paletização']['N Camada Pallet']}")
        print(f"Paletização - N° Cx p/ Pallet: {detalhes['Paletização']['N CX Pallet']}")
        sleep(1)
    print('-=' * 80)
    print("Em 5 segundos você poderá escolher novamente outra função.")
    sleep(5)
    main()


def convert_kg():  # Função responsável por converter kg em Qtd de Cx
    print("Você selecionou: 1 - Obter Peso total em Kg, quantidade de caixas e pallets.")
    sleep(1)
    qtd_itens = int(input("\nInforme a quantidade de itens/produtos no total: "))
    qtd_cx = 0
    kg_sku = 0
    contz = 0
    for cont in range(0, qtd_itens):
        while contz < qtd_itens:
            prod = str(input("\nInforme os três ultímos digitos do código do produto desejado: "))
            achou = False
            for chave in produtos:
                if prod == chave:
                    achou = True
                    kg_sku = int(input("\nInforme a quantidade de kg do produto {0}: "
                                       .format(produtos[chave]['Descrição'])))
                    qtd_cx = qtd_cx + (kg_sku / produtos[chave]['Unidade']['Peso Bruto g/kg'])
                    print("\n{0}".format("-*-" * 32))
                    contz += 1
                if not achou:
                    print("\nProduto não encontrado. Tente novamente")
                    sleep(1)

main()
