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

def ler(arquivo):
  try:
    fp = open(arquivo, 'r', encoding="utf-8")
    linhas = fp.readlines()
    fp.close()
  except IOError as err:
    print("Não foi possível ler o arquivo " + arquivo)
    print(err)
    return False
  return linhas

# VALIDAÇÃO DE ATRIBUTOS:
# Checagem de Atributos:
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

# Valida que a data ou a hora contém apenas dígitos, desprezando espaços
# extras no início e no fim.
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
  return ((len(pri) == 3) and (pri[0] == '(') and (pri[1].upper() in alfabeto) and (pri[2] == ')'))

# Valida a hora. Consideramos que o dia tem 24 horas, como no Brasil, ao invés
# de dois blocos de 12 (AM e PM), como nos EUA.
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
    if (ano < 1000) or (ano > 9999) or (mes < 1) or (mes > 12) or (dia < 1) or (dia > 31):
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

# MANIPULAÇÕES DIVERSAS:

def formataData(data):
  dataFormatada = ''
  if data != '':
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    dataFormatada = '/'.join([dia, mes, ano])
  return dataFormatada

def formataHora(horario):
  horaFormatada = ''
  if horario != '':
    hora = horario[:2]
    minuto = horario[2:]
    horaFormatada = ':'.join([hora, minuto])
  return horaFormatada

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

# printCores('Oi mundo!', RED)
def printCores(texto, cor) :
  print(cor + texto + RESET)

# converte uma data e hora do formato 'ddmmaaaa', 'hhmm' para um inteiro aaaammddhhmm
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

# ORDENAÇÕES:
def organizar(linhas):
  itens = []
  for l in linhas:
    l = l.strip() # remove espaços em branco e quebras de linha do começo e do fim
    tokens = l.split() # quebra o string em palavras
    data, hora, pri, contexto, projeto, desc = checaAtributos(tokens)
    itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens

# Recebe uma lista de tuplas no formato [(n, 'item'),...] e ordena os itens de acordo com n
def quickSortPorChave(lista):
  if lista == []:
    return []
  else:
    pivo = lista.pop(0)
    maiores = []
    menores = []
    for x in lista:
      if x[0] >= pivo[0]:
        maiores.append(x)
      else:
        menores.append(x)
    return quickSortPorChave(menores) + [pivo] + quickSortPorChave(maiores)

def ordenarPorDataHora(itens):
  dataseItens = []
  # Cria uma lista que contém um número inteiro derivado da data, seguindo o modelo YYYYMMAAHHmm
  for lin in itens: # l = (desc, (data, hora, pri, cont, projeto))
    data = str(lin[1][0])
    hora = str(lin[1][1])
    dataHora = dataHoraInt(data, hora)
    item = (dataHora, lin) # Cria uma tupla com o número ordenador e os objetos da linha
    dataseItens.append(item)
  listaOrdenada = quickSortPorChave(dataseItens)
  i = 0
  while i < len(listaOrdenada):
    listaOrdenada[i] = listaOrdenada[i][1]
    i += 1
  return listaOrdenada

def ordenarPorPrioridade(itens):
  prieItens = []
  for linha in itens:
    pri = linha[1][2]
    if pri == '': # No caso de não haver prioridade será atribuída a menor possível
      letra = 'Z'
    else:
      letra = pri[1].upper() # Extrai apenas a letra de '(L)'
    item = (letra, linha)
    prieItens.append(item)
  listaOrdenada = quickSortPorChave(prieItens)
  i = 0
  while i < len(listaOrdenada):
    listaOrdenada[i] = listaOrdenada[i][1]
    i += 1
  return listaOrdenada

# FUNCIONALIDADES:
def adicionar(descricao, extras):
  # não é possível adicionar uma atividade que não possui descrição.
  if descricao  == '':
    return False
  else:
    data, hora, pri, contexto, projeto = checaAtributos(extras)[:5]
    novaAtividade = ' '.join([data, hora, pri, descricao, contexto, projeto])
    novaAtividade = ' '.join(novaAtividade.split()) # Remove espaços duplos
    # Escreve no TODO_FILE.
    try:
      fp = open(TODO_FILE, 'a')
      fp.write(novaAtividade + "\n")
      fp.close()
    except IOError as err:
      print("Não foi possível escrever para o arquivo " + TODO_FILE)
      print(err)
      return False
    return True

def listar():
  linhas = ler(TODO_FILE)
  linhas = organizar(linhas)
  linhas = ordenarPorDataHora(linhas)
  linhas = ordenarPorPrioridade(linhas)
  # Imprime cada linha de forma ordenada, numerada e colorida
  lstOrdenada = []
  i = 0
  while i < len(linhas):
    l = linhas[i]
    desc = l[0]
    data = formataData(l[1][0])
    hora = formataHora(l[1][1])
    pri = l[1][2].upper()
    cont = l[1][3]
    proj = l[1][4]
    cor = colore(pri)
    linha = ' '.join([data, hora, pri, desc, cont, proj])
    linha = ' '.join(linha.split()) # para remover espaços duplos
    lstOrdenada.append(linha)
    printCores(linha, cor)
    i += 1

def remover(num):
  return

def fazer(num):
  return

def priorizar(num, prioridade):
  return

# FUNÇÃO PRINCIPAL:
def processarComandos(comandos) :
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'a'
    print(comandos)
    itemParaAdicionar = organizar([' '.join(comandos)])[0] # recebe uma string separada por espaços
    print(itemParaAdicionar)
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # (descricao, (data, hora, pri, contexto, projeto))
  elif comandos[1] == LISTAR:
    listar()
  elif comandos[1] == REMOVER:
    return
  elif comandos[1] == FAZER:
    return
  elif comandos[1] == PRIORIZAR:
    return
  else :
    print("Comando inválido.")

#processarComandos(sys.argv) # sys.argv = ['agenda.py', 'a', 'Mudar', 'de', 'nome']
