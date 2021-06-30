from os import system
from random import choice
from time import sleep

def nomesSorteados():
    #Os nomes são escritos para cada máquina, todas as vezes que a função for chamada, assim sobrescrevendo os nomes já existentes
    #Para adicionar um novo nome basta coloca-lo nesta lista de nomes a baixo que ele será escrito e poderá ser sorteado junto com os outros
    nomes = ['Senador Salgado Filho', 'Marc Márquez', 'Maverick Viñales', 'Pol Espargaró', 'Fabio Quartararo', 'Miguel Oliveira', 'Jack Miller', 'Jorge Lorenzo']
    with open('Nomes.txt', 'w') as arquivo:
        for nome in nomes:
            arquivo.write(nome + '\n')
    arquivo.close()

    nicks = []
    with open('Nomes.txt', 'r') as leitura:
        for i in leitura:
            nicks.append(i)
    leitura.close()
    sorteadoNick = choice(nicks)
    return sorteadoNick
    
def matrizLetras(mediaLetra, letra):
    lin = mediaLetra
    col = mediaLetra
    matriz = []
    linha = [' '] * col
    i = 0

    if letra == 'X':
        while i < lin:
            matriz.append(linha.copy())
            j = 0
            while j < col:
                if i == j:
                    matriz[i][j] = '\033[35m*\033[m'
                j += 1
            i += 1
        numMax = col - 1
        k = 0
        while True:
            matriz[k][numMax] = '\033[35m*\033[m'
            k += 1
            numMax -= 1
            if numMax == -1:
                break
    elif letra == 'L':
        cont = 0
        valorMax = mediaLetra - 1
        reduz = mediaLetra - 1
        while cont < mediaLetra:
            matriz.append(linha.copy())
            if cont == valorMax:
                while reduz >= 0:
                    matriz[valorMax][reduz] = '\033[35m*\033[m'
                    reduz -= 1
            elif cont != valorMax:
                matriz[cont][0] = '\033[35m*\033[m'
            cont += 1
    elif letra == 'O':
        cont = 0
        j = 0
        valorLimit = mediaLetra - 1
        while cont < mediaLetra:
            matriz.append(linha.copy())
            if cont == 0:
                while i < mediaLetra:
                    matriz[cont][i] = '\033[35m*\033[m'
                    i += 1
            elif cont != valorLimit and cont != 0:
                matriz[cont][0] = '\033[35m*\033[m'
                matriz[cont][valorLimit] = '\033[35m*\033[m'
            else:
                while j < mediaLetra:
                    matriz[cont][j] = '\033[35m*\033[m'
                    j += 1
            cont += 1

    for l in matriz:
        for n in l:
            print(n, end='')
        print()

def biblioteca():
    system('cls')
    livros = {
        'o lobo de wall street':{
            'ano': '2014', 'autor': 'Jordan Belfort', 'editora': 'planeta'
        },
        'vermelho, branco e sangue azul':{
            'ano': '2019', 'autor': 'Casey McQuiston', 'editora': 'Seguinte'
        },
        'as crônicas de narnia':{
            'ano': '2009', 'autor': 'C. S. Lewis', 'editora': 'WMF Martins Fontes'
        },
        'o menino do pijama listrado':{
            'ano': '2007', 'autor': 'John Boyne', 'editora': 'Seguinte'
        },
        'o diário de anne frank':{
            'ano': '1995', 'autor': 'Anne Frank', 'editora': 'Record'
        }
    }
    for i in livros:
        i.title()
        print(i, '\n')

    sleep(10)

    def leitura(leitura):
        print('\nSobre o livro {}'.format(leitura))
        print('Lançado no ano de: ',livros[leitura]['ano'])
        print('Escrito por: ',livros[leitura]['autor'])
        print('Distribuido pela editora: ',livros[leitura]['editora'])
        sleep(10)

    print('Por favor digite o nome igual apareceu para você!')
    livro = input('Por favor digite o nome do livro: ').lower()

    if livro == 'o lobo de wall street':
        leitura('o lobo de wall street')
    elif livro == 'vermelho, branco e sangue azul':
        leitura('vermelho, branco e sangue azul')
    elif livro == 'as crônicas de narnia':
        leitura('as crônicas de narnia')
    elif livro == 'o menino do pijama listrado':
        leitura('o menino do pijama listrado')
    elif livro == 'o diário de anne frank':
        leitura('o diário de anne frank')
    else:
        print('Por favor digite um livro válido')

while True:
    system('cls')
    print('Escolha uma das opções abaixo!')
    print('''
    1 - Abrir arquivo e sortear nome

    2 - Mostrar matriz de letras

    3 - Biblhoteca literária

    4 - Fechar o programa
    ''')
    opcao = input('Digite a sua opção: ')
    if opcao == '1':
        print('O nome sorteado foi: \033[34m', nomesSorteados(), '\033[m')
        sleep(10)
    elif opcao == '2':
        while True:
            letra = input('Por favor escolha uma letra entre (L, X ou O): ').upper()
            dimensao = int(input('Por favor digite a dimensão da letra: ps: A dimensão precisa ser maior que 2: '))
            if letra == 'L' or letra == 'X' or letra == 'O' and dimensao > 2:
                matrizLetras(dimensao, letra)
                sleep(15)
                break
            else:
                print('Por favor digite valores válidos!')
    elif opcao == '3':
        biblioteca()
    elif opcao == '4':
        print('Obrigado por utilizar os nossos serviços!')
        print('\033[31mEncerrando...\033[m')
        sleep(4)
        break
    else:
        print('Por favor digite uma opção válida')
        sleep(4)