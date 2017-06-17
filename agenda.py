import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED = "\033[1;31m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'
AJUDA = 'h'

''' MANIPULAÇÕES DIVERSAS '''
def lerArquivo(arquivo):
    try:
        fp = open(arquivo, 'r', encoding="latin-1")#, encoding="utf-8")
        linhas = fp.readlines()
        fp.close()
    except IOError as err:
        try:
          fp = open(arquivo, 'w')#, encoding="latin-1")#, encoding="utf-8")
          linhas = []
          fp.close()
        except IOError as err:
          print("Não foi possível ler o arquivo " + arquivo)
          print(err)
          return False
    return linhas

def escreverArquivo(texto, arquivo):
    try:
        fp = open(arquivo, 'a')
        fp.write(texto + "\n")
        fp.close()
    except IOError as err:
        print("Não foi possível escrever para o arquivo " + arquivo)
        print(err)
        return False

def atualizarArquivo(lista, arquivo):
    try:
        fp = open(arquivo, 'w+')
        fp.seek(0)
        for x in lista:
            fp.write(x)
        fp.close()
    except IOError as err:
        print("Não foi possível atualizar o arquivo " + arquivo)
        print(err)
        return False

# Recebe uma data no formato 'DDMMAAAA' e transforma em 'DD/MM/AAAA'
def formataData(data):
    dataFormatada = ''
    if data != '':
        dia = data[:2]
        mes = data[2:4]
        ano = data[4:]
        dataFormatada = '/'.join([dia, mes, ano])
    return dataFormatada

# Recebe um horário no formato 'HHmm' e transforma em 'HH:mm'
def formataHora(horario):
    horaFormatada = ''
    if horario != '':
        hora = horario[:2]
        minuto = horario[2:]
        horaFormatada = ':'.join([hora, minuto])
    return horaFormatada

# Paleta de cores de acordo com a prioridade
def colore(prioridade):
    if prioridade == '':
        return RESET
    else:
        letra = prioridade[1]
        if letra == 'A':
            cor = RED
        elif letra == 'B':
            cor = YELLOW
        elif letra == 'C':
            cor = CYAN
        elif letra == 'D':
            cor = GREEN
        else:
            cor = RESET
    return cor

# PrintCores('Oi mundo!', RED)
def printCores(texto, cor) :
    print(cor + texto + RESET)

# Recebe data e hora no formato 'DDMMAAAA' e 'HHmm'
# e retorna um inteiro AAAAMMDDHHmm (campos faltantes preenchidos com '9')
def dataHoraInt(data, hora):
    if data == '':
        dataInteiro = '99999999'
    else:
        ano = data[4:]
        mes = data[2:4]
        dia = data[:2]
        dataInteiro = ano + mes + dia
    if hora == '':
        horaInteiro = '9999'
    else:
        horaInteiro = hora
    return int(dataInteiro + horaInteiro)

# Função que transforma uma tupla (ordenador, (objetos))
# em (objetos)
def removeOrdenador(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i][1]
        i += 1
    return lista

def numValido(n):
    if soDigitos(n) and int(n) > 0:
        return int(n)
    return False

''' VALIDAÇÃO DE ATRIBUTOS '''
# Função que chama as demais funções de validação.
# Se não for um atributo válido então anexa à descrição.
def checaAtributos(lista):
    data, hora, pri, contexto, projeto, desc = ['' for x in range(6)]
    i = 0
    while i < len(lista):
        if i == 0 and data == '' and dataValida(lista[i]):
            data = lista[i]
        elif i <= 1 and hora == '' and horaValida(lista[i]):
            hora = lista[i]
        elif i <= 2 and pri == '' and prioridadeValida(lista[i]):
            pri = lista[i]
        elif i >= len(lista) - 2 and contexto == '' and contextoValido(lista[i]):
            contexto = lista[i]
        elif i == len(lista) - 1 and projeto == '' and projetoValido(lista[i]):
            projeto = lista[i]
        else:
            desc = desc + ' ' + lista[i]
        i += 1
    if desc == ''.join([data, hora, pri, contexto, projeto]):
        desc = ''
    return (data, hora, pri, contexto, projeto, desc)
'''
def checaAtributos(lista):
    data, hora, pri, contexto, projeto, desc = ['' for x in range(6)]
    pref = 0
    if dataValida(lista[pref]):
        data = lista[pref]
        if pref < len(lista) - 1:
            pref += 1
    if horaValida(lista[pref]):
        hora = lista[pref]
        if pref < len(lista) - 1:
            pref += 1
    if prioridadeValida(lista[pref]):
        pri = lista[pref]
        if pref < len(lista) - 1:
            pref += 1
    suf = len(lista) - 1
    if projetoValido(lista[suf]):
        projeto = lista[suf]
        if suf > 1:
            suf -= 1
    if contextoValido(lista[suf]):
        contexto = lista[suf]
        if suf > 1:
            suf -= 1
    desc = lista[pref:suf+1]
    desc = ' '.join(desc)
    if desc == ''.join([data, hora, pri, contexto, projeto]):
        desc = ''
    return (data, hora, pri, contexto, projeto, desc)
'''   
# Valida que a data ou a hora contém apenas dígitos, desprezando
# espaços extras no início e no fim.
def soDigitos(numero) :
    if type(numero) != str :
        return False
    for x in numero :
        if x < '0' or x > '9' :
            return False
    return True

# Valida a prioridade.
def prioridadeValida(pri):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ((len(pri) == 3) and (pri[0] == '(')
            and (pri[1].upper() in alfabeto) and (pri[2] == ')'))

# Valida a hora. Consideramos que o dia tem 24 horas, como no Brasil,
# ao invés de dois blocos de 12 (AM e PM), como nos EUA.
def horaValida(horaMin) :
    if len(horaMin) != 4 or not soDigitos(horaMin):
        return False
    else:
        horas = int(horaMin[:2])
        minutos = int(horaMin[2:])
        if (horas < 0) or (minutos < 0) or (horas > 23) or (minutos > 59):
          return False
    return True

# Valida datas. Verificar inclusive se não estamos tentando
# colocar 31 dias em fevereiro. Não precisamos nos certificar, porém,
# de que um ano é bissexto.
def dataValida(data):
    mes30 = [4, 6, 9, 11]
    if len(data) != 8 or not soDigitos(data):
        return False
    else:
        dia = int(data[:2])
        mes = int(data[2:4])
        ano = int(data[4:])
        if ((ano < 1000) or (ano > 9999) or (mes < 1) or (mes > 12)
            or (dia < 1) or (dia > 31)):
          return False
        elif (mes == 2 and dia > 29) or ((mes in mes30) and dia == 31):
          return False
    return True

# Valida que o string do projeto está no formato correto.
def projetoValido(proj):
    return ((len(proj) > 1) and (proj[0] == '+'))

# Valida que o string do contexto está no formato correto.
def contextoValido(cont):
    return ((len(cont) > 1) and (cont[0] == '@'))

''' ORDENAÇÕES '''
def organizar(linhas):
    itens = []
    for l in linhas:
        l = l.strip() # remove espaços em branco e quebras de linha
        tokens = l.split() # quebra o string em palavras
        data, hora, pri, contexto, projeto, desc = checaAtributos(tokens)
        itens.append((desc, (data, hora, pri, contexto, projeto)))
    return itens

# Quicksort recursivo para ordenar uma lista de tuplas
# no formato [(n, (numLin, (objeto)))...] por 'n'
def quickSortPorChave(lista):
    if lista == []:
        return []
    else:
        pivo = lista.pop(0) # O pivô tem que ser toda a tupla (n, (objeto))
        maiores = []
        menores = []
        for x in lista: # Apenas a condicional precisa levar em conta o 'n'
            if x[0] >= pivo[0]: 
                maiores.append(x)
            else:
                menores.append(x)
    return quickSortPorChave(menores) + [pivo] + quickSortPorChave(maiores)

def ordenarPorDataHora(itens):
    # Cria temporariamente uma lista de tuplas (ordenador, (atributos))
    dataseItens = []
    for x in itens: # (numLinha, (desc, (data, hora, pri, cont, projeto)))
        data = str(x[1][1][0])
        hora = str(x[1][1][1])
        dataHora = dataHoraInt(data, hora) # Inteiro no formato AAAAMMDDHHmm
        item = (dataHora, x) # (dataHora, (numLinha, (desc, (data, hora, (...)
        dataseItens.append(item)
    dataseItens = quickSortPorChave(dataseItens)
    # Remove o objeto ordenador da lista final
    listaOrdenada = removeOrdenador(dataseItens)
    return listaOrdenada

def ordenarPorPrioridade(itens):
    # Cria temporariamente uma lista de tuplas (ordenador, (atributos))
    prieItens = []
    for x in itens:
        pri = x[1][1][2] # (numLinha, (desc,(data,hora,"pri",(...)))
        if pri == '':
            letra = 'Z' # No caso de não haver prioridade definida
        else:
            letra = pri[1].upper() # Extrai apenas a letra de '("X")'
        item = (letra, x) # (letra, (numLinha, (desc, (data, hora, (...)))))
        prieItens.append(item)
    prieItens = quickSortPorChave(prieItens)
    # Remove o objeto ordenador da lista final
    listaOrdenada = removeOrdenador(prieItens)
    return listaOrdenada

''' FUNCIONALIDADES '''
def adicionar(desc, extras):
    # Não é possível adicionar uma atividade que não possui descrição.
    if desc  == '':
        return False
    else:
        data, hora, pri, contexto, projeto = extras
        novaAtividade = ' '.join([data, hora, pri, desc, contexto, projeto])
        novaAtividade = ' '.join(novaAtividade.split()) # Remove espaços duplos
        # Escreve no TODO_FILE.
        escreverArquivo(novaAtividade, TODO_FILE)
    return True

# Função que lista todas as linhas no arquivo TODO_FILE
# coloridas por prioridade e ordenadas
def listar():
    lin = lerArquivo(TODO_FILE) # ['texto linha 1\n', 'texto linha 2\n', (...)]
    if lin == False:
        return False # O programa falhou em ler o arquivo TODO_FILE
    lin = organizar(lin) # ['('desc', ('attr1','attr2', (...)))', (...)]
    # Laço para anexar o número da linha no arquivo às informações
    linEnumLin = []
    n = 1
    for x in lin:
        linEnumLin.append((n, x)) #(n, ('desc', ('attr1', 'attr2', ...)))
        n += 1
    linEnumLin = ordenarPorDataHora(linEnumLin)
    linEnumLin = ordenarPorPrioridade(linEnumLin)
    # Formata e imprime, uma a uma, as linhas do TODO_FILE
    i = 0
    while i < len(linEnumLin):
        num = '{:02d}'.format(linEnumLin[i][0])
        l = linEnumLin[i][1] # Para simplificar as demais linhas
        desc = l[0]
        data = formataData(l[1][0]) # 'dd/mm/aaaa'
        hora = formataHora(l[1][1]) # 'hh:mm'
        pri = l[1][2].upper()
        cont = l[1][3]
        proj = l[1][4]
        cor = colore(pri) # Colore de acordo com a prioridade
        linha = ' '.join([num, data, hora, pri, desc, cont, proj])
        linha = ' '.join(linha.split()) # Remove espaços duplos
        printCores(linha, cor)
        i += 1
    return True

def remover(num):
    linhas = lerArquivo(TODO_FILE)
    if num > len(linhas):
        return False
    removido = linhas.pop(num-1)
    a = atualizarArquivo(linhas, TODO_FILE)
    if a == False:
        return False
    return removido

def fazer(num):
    r = remover(num)
    if r != False:
        feito = r.strip()
        e = escreverArquivo(feito, ARCHIVE_FILE)
        if e == False:
            return False
    else:
        return False
    return True

def priorizar(num, pri):
    prioridade = '(' + pri + ')'
    if not(prioridadeValida(prioridade)):
        return False
    linhas = lerArquivo(TODO_FILE)
    if num > len(linhas):
        return False
    linha = linhas[num-1].split()
    # Laço para checar se a linha já tem uma prioridade definida
    # Se tiver, substitui. Se não, põe a prioridade na posição adequada
    priorizado = False
    i = 0
    while i < len(linha) and not(priorizado):
       if prioridadeValida(linha[i]):
           linha[i] = prioridade
           priorizado = True
       i += 1
    if not(priorizado):
        pos = 0
        if dataValida(linha[pos]):
            pos += 1
        if horaValida(linha[pos]):
            pos += 1
        linha = linha[:pos] + [prioridade] + linha[pos:]
    linha = ' '.join(linha)
    linhas[num-1] = linha + '\n' #.strip() inicial retirou o \n
    atualizarArquivo(linhas, TODO_FILE)
    return True

def ajuda():
    print("\nFormas de uso da agenda.py: (sem aspas ou parênteses)\n\n"
          "- Adicionar: 'python agenda.py a (atividade)' (a atividade precisa "
         "conter ao menos um caracter).\n"
         "- Listar: 'python agenda.py l' (O arquivo todo.txt precisa estar "
         "presente na mesma pasta que o agenda.py).\n"
         "- Remover: 'python agenda.py r (n)' (n deve ser o número da linha "
         "da atividade a remover).\n"
         "- Fazer: 'python agenda.py f (n)' (n deve ser o número da linha "
         "da atividade a fazer).\n"
         "- Priorizar: 'python agenda.py p (n) (L)' (n deve ser o número "
         "da linha a priorizar, L deve ser uma letra entre A-Z).\n")
    return True

def processarComandos(cmd):
    executado = False
    if len(cmd) > 1:
        if cmd[1] == ADICIONAR:
            cmd.pop(0) # Remove 'agenda.py'
            cmd.pop(0) # Remove 'a'
            itemParaAdicionar = organizar([' '.join(cmd)])[0]
            executado = adicionar(itemParaAdicionar[0], itemParaAdicionar[1])
            if executado:
                print("Atividade adicionada.")
        elif cmd[1] == LISTAR:
            executado = listar() # Imprime na tela a lista formatada
        elif cmd[1] == REMOVER: # esperado ['agenda.py', 'r', 'n']
            if len(cmd) == 3:
                n = numValido(cmd[2])
                if n != False:
                    executado = remover(n)
                    if executado:
                        print("Atividade removida.")
        elif cmd[1] == FAZER: # ['agenda.py', 'f', 'n']
            if len(cmd) == 3:
                n = numValido(cmd[2])
                if n != False:
                    executado = fazer(n)
                    if executado:
                        print("Atividade feita.")
        elif cmd[1] == PRIORIZAR: # ['agenda.py', 'p', 'n', 'prioridade']
            if len(cmd) == 4:
                n = numValido(cmd[2])
                if n != False:
                    pri = cmd[3].upper()
                    executado = priorizar(n, pri)
                    if executado:
                        print("Atividade priorizada.")
        elif cmd[1] == AJUDA:
            executado = ajuda()
    if not(executado):
        print("Houve um erro com sua solicitação.\n"
            "Caso você precise de ajuda tente o comando 'python agenda.py h'")

processarComandos(sys.argv) # ['agenda.py', 'a', 'Mudar', 'de', 'nome']
