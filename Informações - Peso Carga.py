from math import ceil
from openpyxl import load_workbook
from os import path, remove
from pandas import DataFrame, ExcelWriter
from pyautogui import alert, confirm, prompt

produtos = { # Dicionário com todos os produtos cadastrados
    '060': {
        'Descrição': 'Goiabada Ramy Fl 300g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto Kg': 7.36
        },
        'Paletização': {
            'N CX Camada': 13,
            'N Camada Pallet': 9,
            'N CX Pallet': 117
        }
    },
    '140': {
        'Descrição': 'Ketchup Tradicional Ramy Mini Sachê 7g',
        'Peso Nominal g/kg': 7,
        'Cx Embarque': {
            'Quantidade': 144,
            'Peso Bruto Kg': 1.05
        },
        'Paletização': {
            'N CX Camada': 36,
            'N Camada Pallet': 11,
            'N CX Pallet': 396
        }
    },
    '141': {
        'Descrição': 'Maionese Tradicional Ramy Mini Sachê 7g',
        'Peso Nominal g/kg': 7,
        'Cx Embarque': {
            'Quantidade': 144,
            'Peso Bruto Kg': 1.05
        },
        'Paletização': {
            'N CX Camada': 36,
            'N Camada Pallet': 11,
            'N CX Pallet': 396
        }
    },
    '142': {
        'Descrição': 'Mostarda Ramy Mini Sachê 7g',
        'Peso Nominal g/kg': 7,
        'Cx Embarque': {
            'Quantidade': 144,
            'Peso Bruto Kg': 1.05
        },
        'Paletização': {
            'N CX Camada': 36,
            'N Camada Pallet': 11,
            'N CX Pallet': 396
        }
    },
    '571': {
        'Descrição': 'Maionese Tradicional Ramy Sachê Bico 180g',
        'Peso Nominal g/kg': 180,
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto Kg': 6.35
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '580': {
        'Descrição': 'Molho de Tomate Trad. Ramy Sachê 300g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '581': {
        'Descrição': 'Molho de Tomate Peneirado Ramy Sachê 300g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '582': {
        'Descrição': 'Extrato de Tomate Ramy Sachê 300g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '587': {
        'Descrição': 'Molho de Tomate Manjericão Ramy Sachê 300g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '588': {
        'Descrição': 'Molho de Tomate Pizza Ramy Sachê Bico 180g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '589': {
        'Descrição': 'Molho de Tomate Ervas Finas Ramy Sachê 300g',
        'Peso Nominal g/kg': 300,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 11.36
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '690': {
        'Descrição': 'Molho de Tomate Trad. Ramy Sachê 1,7 Kg',
        'Peso Nominal g/kg': 1700,
        'Cx Embarque': {
            'Quantidade': 6,
            'Peso Bruto Kg': 10.88
        },
        'Paletização': {
            'N CX Camada': 10,
            'N Camada Pallet': 7,
            'N CX Pallet': 70
        }
    },
    '785': {
        'Descrição': 'Ketchup Ramy Trad. Frs 400g',
        'Peso Nominal g/kg': 400,
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto Kg': 10.48
        },
        'Paletização': {
            'N CX Camada': 11,
            'N Camada Pallet': 6,
            'N CX Pallet': 66
        }
    },
    '787': {
        'Descrição': 'Mostarda Ramy Frs 190g',
        'Peso Nominal g/kg': 190,
        'Cx Embarque': {
            'Quantidade': 24,
            'Peso Bruto Kg': 5.23
        },
        'Paletização': {
            'N CX Camada': 15,
            'N Camada Pallet': 7,
            'N CX Pallet': 105
        }
    },
    '789': {
        'Descrição': 'Ketchup de Tomate Trad. Ramy Sachê Bico 180g',
        'Peso Nominal g/kg': 180,
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto Kg': 6.35
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '790': {
        'Descrição': 'Molho Mostarda Ramy Sachê Bico 180g',
        'Peso Nominal g/kg': 180,
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto Kg': 11.42
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '791': {
        'Descrição': 'Molho Barbecue Ramy Sachê Bico 180g',
        'Peso Nominal g/kg': 180,
        'Cx Embarque': {
            'Quantidade': 32,
            'Peso Bruto Kg': 6.35
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 7,
            'N CX Pallet': 112
        }
    },
    '792': {
        'Descrição': 'Milho Sachê Ramy 1,7 Kg',
        'Peso Nominal g/kg': 1700,
        'Cx Embarque': {
            'Quantidade': 6,
            'Peso Bruto Kg': 17.18
        },
        'Paletização': {
            'N CX Camada': 7,
            'N Camada Pallet': 6,
            'N CX Pallet': 42
        }
    },
    '882': {
        'Descrição': 'Milho Verde em Conserva Ramy Sachê 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '883': {
        'Descrição': 'Dueto em Conserva Ramy Sachê 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '884': {
        'Descrição': 'Ervilha em Conserva Ramy Sachê 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '885': {
        'Descrição': 'Seleta de Legumes em Conserva Ramy Sachê 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 36,
            'Peso Bruto Kg': 9.72
        },
        'Paletização': {
            'N CX Camada': 16,
            'N Camada Pallet': 6,
            'N CX Pallet': 96
        }
    },
    '886': {
        'Descrição': 'Milho Crocante ao Vapor Ramy Lt 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 30,
            'Peso Bruto Kg': 7.15
        },
        'Paletização': {
            'N CX Camada': 6,
            'N Camada Pallet': 18,
            'N CX Pallet': 108
        }
    },
    '887': {
        'Descrição': 'Ervilha Crocante ao Vapor Ramy Lt 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 30,
            'Peso Bruto Kg': 7.15
        },
        'Paletização': {
            'N CX Camada': 6,
            'N Camada Pallet': 18,
            'N CX Pallet': 108
        }
    },
    '888': {
        'Descrição': 'Dueto Crocante ao Vapor Ramy 170g',
        'Peso Nominal g/kg': 170,
        'Cx Embarque': {
            'Quantidade': 30,
            'Peso Bruto Kg': 7.15
        },
        'Paletização': {
            'N CX Camada': 6,
            'N Camada Pallet': 11,
            'N CX Pallet': 108
        }
    }
}

def gerar_planilha(funcao, nome, df): # Função utilizada para gerar um arquivo Excel com os dados do DataFrame
    desktop = path.join(path.expanduser('~'), 'Desktop')
    caminho = path.join(desktop, nome)

    try: # Tratamento de erro para caso o arquivo já exista
        if path.exists(caminho):
            remove(caminho)
    except Exception as e:
        alert(f"Erro ao tentar remover o arquivo existente: {e}", title='ERROR - Calculo de Peso Carga')

    if funcao == 1:
        descricao_valores = {
            'Descrição': ['Peso Total da Carga (Kg)', 'Volume Total Caixas', 'Quantidade Total Pallets', 'Peso Total da Carga com Pallets (Kg)'],
            'Valores': [df[col].sum() for col in ['Peso Total da Carga (Kg)', 'Volume Total Caixas', 'Quantidade Total Pallets', 'Peso Total da Carga com Pallets (Kg)']]
        }
        
        desc_val_df = DataFrame(descricao_valores)
        with ExcelWriter(caminho, engine='openpyxl', mode='w') as writer:
            desc_val_df.to_excel(writer, sheet_name='Dados', index=False)
            workbook = writer.book
            worksheet = writer.sheets['Dados']
            worksheet.column_dimensions['A'].width = 35
            worksheet.column_dimensions['B'].width = 15
    elif funcao == 2:
        df = DataFrame.from_dict(df, orient='index')
        df.to_excel(caminho, index=False)
    return caminho


def main():  # Função principal, utilizada para iniciar o programa
    opcao = int((confirm(text="""Selecione a opção desejada:
                                         
1 - Obter Peso total em Kg, quantidade de caixas e pallets.
2 - Ver todos os itens cadastrados.
3 - Obter quantidade de caixas a partir do peso em gramas.
                                         
9 - Encerra o programa.""", title='Calculo de Peso Carga', buttons=['1', '2', '3', '9'] )))
    menu(opcao)


def menu(opcao):  # Função utilizada para acessar o menu e definir o próximo passo do programa
    match opcao:
        case 1:
            calc_peso_vol()
        case 2:
            relatorio_prods()
        case 3:
            convert_kg()
        case 9:
            alert("Obrigado por utilizar o programa.", title='Calculo de Peso Carga', button='OK')


def calc_peso_vol():  # Função utilizada para calcular o peso total do pedido em kg, volume e quantidade de pallets
    while True: # Laço de repetição para caso o usuário digite um valor inválido
        try: # Tratamento de erro para caso o usuário digite um valor inválido
            qtd_itens = int(prompt(
                text="""Você selecionou: 1 - Obter Peso total em Kg, quantidade de caixas e pallets.
                
                Informe a quantidade de SKUs no total:""", title='Calculo de Peso Carga', default='0'))
            soma = 0
            volume = 0
            cont = 0
            pallets = 0
            outras_cxs = 0
            while cont < qtd_itens:
                while True: # Laço de repetição para caso o usuário digite um valor inválido
                    try: # Tratamento de erro para caso o usuário digite um valor inválido
                        prod = prompt(text="Informe os três ultímos digitos do código do produto desejado: ",
                                        title='Calculo de Peso Carga', default='000')
                        achou = False
                        for chave in produtos:
                            if str(prod) == chave:
                                achou = True
                                while True: # Laço de repetição para caso o usuário digite um valor inválido
                                    try: # Tratamento de erro para caso o usuário digite um valor inválido
                                        qtd_cx = int(prompt(text=f"Informe a quantidade de caixas do produto {produtos[chave]['Descrição']}: ",
                                                                    title='Calculo de Peso Carga', default='0'))
                                        if qtd_cx >= produtos[chave]['Paletização']['N CX Pallet']:
                                            pallets = pallets + int((qtd_cx / produtos[chave]['Paletização']['N CX Pallet']))
                                            if qtd_cx % int(produtos[chave]['Paletização']['N CX Pallet']):
                                                outras_cxs = outras_cxs + (qtd_cx % int(produtos[chave]['Paletização']
                                                                                        ['N CX Pallet']))
                                        else:
                                            outras_cxs = outras_cxs + qtd_cx
                                        soma = soma + (qtd_cx * produtos[chave]['Cx Embarque']['Peso Bruto Kg'])
                                        volume = volume + qtd_cx
                                        cont += 1
                                        break
                                    except ValueError:
                                        alert(text="Você digitou um valor inválido. Tente novamente.",
                                                  title='Calculo de Peso Carga')
                        if not achou:
                            alert(text="Produto não encontrado. Tente novamente", title='Calculo de Peso Carga')
                        break
                    except ValueError:
                        alert(text="Você digitou um valor inválido. Tente novamente.", title='Calculo de Peso Carga')
            qtd_pallets = pallets + (ceil(outras_cxs / 96))
            peso_final = soma + (qtd_pallets * 30)
            carga = DataFrame({
                'Peso Total da Carga (Kg)': [soma],
                'Volume Total Caixas': [volume],
                'Quantidade Total Pallets': [qtd_pallets],
                'Peso Total da Carga com Pallets (Kg)': [peso_final]
            })
            confirm(text=f"""Peso total da carga: {soma:.2f} Kg
Volume total da carga: {volume} caixas
Quantidade total de pallets da carga: {qtd_pallets}
Peso total da carga com os pallets: {peso_final:.2f} Kg
                        """, title='Calculo de Peso Carga')
            gerar_plan = confirm(text="Deseja gerar um relatório com os dados da carga?",
                                     title='Calculo de Peso Carga', buttons=['Sim', 'Não'])
            if gerar_plan == 'Sim':
                alert(text=f"""Um arquivo Excel com os dados da carga foi gerado em: {gerar_planilha(1, 'Carga.xlsx', carga)}""",
                          title='Calculo de Peso Carga')
            break
        except ValueError as e:
            alert(text=f"""Você digitou um valor inválido. Tente novamente.
Erro: {e}. """, title='Calculo de Peso Carga')
    main()


def relatorio_prods():  # Função responsável por gerar um relatório com todos os produtos cadastrados
    alert(text=f"""Você selecionou: 2 - Ver todos os itens cadastrados.
    
Um arquivo Excel com todos os produtos cadastrados foi gerado em: {gerar_planilha(2, 'Produtos.xlsx', produtos)}""",
title='Calculo de Peso Carga')
    main()


def convert_kg():  # Função responsável por converter kg em Qtd de Cx
    while True: # Laço de repetição para caso o usuário digite um valor inválido
        try: # Tratamento de erro para caso o usuário digite um valor inválido
            prod = int(prompt(text="""Você selecionou: 3 - Obter quantidade de caixas a partir do peso em gramas.

        Informe os três ultímos digitos do código do produto desejado: """,
                                  title='Calculo de Peso Carga', default='000'))
            achou = False
            for chave in produtos:
                if str(prod) == chave:
                    achou = True
                    kg_sku = float(prompt(text=f"Informe a quantidade em gramas do produto {produtos[chave]['Descrição']}: ",
                         title='Calculo de Peso Carga', default='0'))
                    unidades = kg_sku / produtos[chave]['Peso Nominal g/kg']
                    caixas = unidades / produtos[chave]['Cx Embarque']['Quantidade']
                    confirm(text=f"Com o peso em gramas informado, serão necessárias aproximadamente: {ceil(caixas)} caixas do item {produtos[chave]['Descrição']}",
                        title='Calculo de Peso Carga')
            if not achou:
                alert(text="Produto não encontrado.", title='Calculo de Peso Carga')
            else:
                break
        except ValueError:
            alert(text="Você digitou um valor inválido. Tente novamente.", title='Calculo de Peso Carga')
    main()


main()
