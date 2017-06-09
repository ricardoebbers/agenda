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

''' MANIPULAÇÕES DIVERSAS '''
# Função genérica para ler um arquivo existente.
def lerArquivo(arquivo):
  try:
    fp = open(arquivo, 'r')#, encoding="utf-8")
    linhas = fp.readlines()
    fp.close()
  except IOError as err:
    print("Não foi possível ler o arquivo " + arquivo)
    print(err)
    return False
  return linhas

# Função genérica para adicionar texto a um arquivo existente
def escreverArquivo(texto, arquivo):
  try:
    fp = open(arquivo, 'a')
    fp.write(texto + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + arquivo)
    print(err)
    return False

# Função auxiliar à listagem, pega uma data no formato 'DDMMAAAA'
# e transforma em 'DD/MM/AAAA'
def formataData(data):
  dataFormatada = ''
  if data != '':
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    dataFormatada = '/'.join([dia, mes, ano]) # 'dd/mm/aaaa'
  return dataFormatada

# Função auxiliar à listagem, pega um horário no formato 'HHmm'
# e transforma em 'HH:mm'
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
      cor = BLUE
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

# Converte uma data e hora do formato 'DDMMAAAA' e 'HHmm'
# para um inteiro AAAAMMDDHHmm
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

''' VALIDAÇÃO DE ATRIBUTOS '''
# Função que chama as demais funções de validação.
# Se não for um atributo válido então anexa à descrição
def checaAtributos(lista):
  data, hora, pri, contexto, projeto, desc = ['' for x in range(6)]
  for x in lista:
    if dataValida(x):
      data = x
    elif horaValida(x):
      hora = x
    elif prioridadeValida(x):
      pri = x
    elif contextoValido(x):
      contexto = x
    elif projetoValido(x):
      projeto = x
    else:
      desc = ' '.join([desc, x])
  return (data, hora, pri, contexto, projeto, desc)

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
    for x in lista:
      if x[0] >= pivo[0]: # Apenas a condicional precisa levar em conta o 'n'
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
    item = (dataHora, x) # (dataHora, (numLinha, (desc, (data, hora, (...)))))
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
def adicionar(descricao, extras):
  # Não é possível adicionar uma atividade que não possui descrição.
  if descricao  == '':
    return False
  else:
    # Faz todas as checagens necessárias dos atributos
    data, hora, pri, contexto, projeto = checaAtributos(extras)[:5]
    # Como a atividade será escrita no TODO_FILE, cria uma string dos atributos
    novaAtividade = ' '.join([data, hora, pri, descricao, contexto, projeto])
    novaAtividade = ' '.join(novaAtividade.split()) # Remove espaços duplos
    # Escreve no TODO_FILE.
    escreverArquivo(novaAtividade, TODO_FILE)
  return True

# Função que lista todas as linhas no arquivo TODO_FILE
# coloridas por prioridade e ordenadas
def listar():
  lin = lerArquivo(TODO_FILE) # ['texto linha 1\n', 'texto linha 2\n', (...)]
  lin = organizar(lin) # ['('desc', ('attr1','attr2', (...)))', (...)]
  # Laço para anexar o número da linha no arquivo à linha
  linEnumLin = []
  n = 1
  for l in lin:
    linEnumLin.append((n, l)) #(n, ('desc', ('attr1', 'attr2', ...)))
    n += 1
  linEnumLin = ordenarPorDataHora(linEnumLin) # Lista de tuplas ordenada por data e hora
  linEnumLin = ordenarPorPrioridade(linEnumLin) # Lista anterior ordenada por prioridade
  # Formata e imprime, uma a uma, as linhas do TODO_FILE
  i = 0
  while i < len(linEnumLin):
    num = str(linEnumLin[i][0])
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

def remover(num):
  return

def fazer(num):
  return

def priorizar(num, prioridade):
  return

def processarComandos(cmd) :
  if cmd[1] == ADICIONAR:
    cmd.pop(0) # Remove 'agenda.py'
    cmd.pop(0) # Remove 'a'
    itemParaAdicionar = organizar([' '.join(cmd)])[0]
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1])
  elif cmd[1] == LISTAR:
    listar() # Imprime na tela a lista formatada
  elif cmd[1] == REMOVER:
    return
  elif cmd[1] == FAZER:
    return
  elif cmd[1] == PRIORIZAR:
    return
  else :
    print("Comando inválido.")

processarComandos(sys.argv) # ['agenda.py', 'a', 'Mudar', 'de', 'nome']
