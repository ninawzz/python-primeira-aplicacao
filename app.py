import os

restaurantes = [
    {'nome': 'praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Al dente', 'categoria': 'Italiano', 'ativo': True},
    {'nome': 'Outback', 'categoria': 'Churrasco', 'ativo': False}
]

def exibir_nome_programa():
    print('SABOR EXPRESS\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado dos Restaurantes')
    print('4. Sair\n')

def cadastrar_restaurantes():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
        'nome': nome_do_restaurante.strip(),
        'categoria': categoria.strip(),
        'ativo': False
    }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f"{nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {status}")
    voltar_menu_principal()

def alternar_estado_restaurantes():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.strip().lower() == restaurante['nome'].strip().lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f"O restaurante {restaurante['nome']} foi ativado com sucesso!"
                if restaurante['ativo']
                else f"O restaurante {restaurante['nome']} foi desativado com sucesso!"
            )
            print(mensagem)
            break

    if not restaurante_encontrado:
        print('Restaurante não encontrado.')

    voltar_menu_principal()

def sair():
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    print('Opção inválida')
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurantes()
        elif opcao_escolhida == 4:
            sair()
        else:
            print('Opção inválida')
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
