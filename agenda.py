import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)
  

# Adiciona um compromisso aa agenda. Um compromisso tem no minimo
# uma descrição. Adicionalmente, pode ter, em caráter opcional, uma
# data (formato DDMMAAAA), um horário (formato HHMM), uma prioridade de A a Z, 
# um contexto onde a atividade será realizada (precedido pelo caractere
# '@') e um projeto do qual faz parte (precedido pelo caractere '+'). Esses
# itens opcionais são os elementos da tupla "extras", o segundo parâmetro da
# função.
#
# extras ~ (data, hora, prioridade, contexto, projeto)
#
# Qualquer elemento da tupla que contenha um string vazio ('') não
# deve ser levado em consideração. 
def adicionar(descricao, extras):

  # não é possível adicionar uma atividade que não possui descrição. 
  if descricao  == '' :
    return False
  

  ################ COMPLETAR


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


# Valida a prioridade.
def prioridadeValida(pri):

  ################ COMPLETAR
  
  return False


# Valida a hora. Consideramos que o dia tem 24 horas, como no Brasil, ao invés
# de dois blocos de 12 (AM e PM), como nos EUA.
def horaValida(horaMin) :
  if len(horaMin) != 4 or not soDigitos(horaMin):
    return False
  else:
    ################ COMPLETAR
    return True

# Valida datas. Verificar inclusive se não estamos tentando
# colocar 31 dias em fevereiro. Não precisamos nos certificar, porém,
# de que um ano é bissexto. 
def dataValida(data) :

  ################ COMPLETAR

  return False

# Valida que o string do projeto está no formato correto. 
def projetoValido(proj):

  ################ COMPLETAR

  return False

# Valida que o string do contexto está no formato correto. 
def contextoValido(cont):

  ################ COMPLETAR

  return False

# Valida que a data ou a hora contém apenas dígitos, desprezando espaços
# extras no início e no fim.
def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True


# Dadas as linhas de texto obtidas a partir do arquivo texto todo.txt, devolve
# uma lista de tuplas contendo os pedaços de cada linha, conforme o seguinte
# formato:
#
# (descrição, prioridade, (data, hora, contexto, projeto))
#
# É importante lembrar que linhas do arquivo todo.txt devem estar organizadas de acordo com o
# seguinte formato:
#
# DDMMAAAA HHMM (P) DESC @CONTEXT +PROJ
#
# Todos os itens menos DESC são opcionais. Se qualquer um deles estiver fora do formato, por exemplo,
# data que não tem todos os componentes ou prioridade com mais de um caractere (além dos parênteses),
# tudo que vier depois será considerado parte da descrição.  
def organizar(linhas):
  itens = []

  for l in linhas:
    data = '' 
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''
  
    l = l.strip() # remove espaços em branco e quebras de linha do começo e do fim
    tokens = l.split() # quebra o string em palavras

    # Processa os tokens um a um, verificando se são as partes da atividade.
    # Por exemplo, se o primeiro token é uma data válida, deve ser guardado
    # na variável data e posteriormente removido a lista de tokens. Feito isso,
    # é só repetir o processo verificando se o primeiro token é uma hora. Depois,
    # faz-se o mesmo para prioridade. Neste ponto, verifica-se os últimos tokens
    # para saber se são contexto e/ou projeto. Quando isso terminar, o que sobrar
    # corresponde à descrição. É só transformar a lista de tokens em um string e
    # construir a tupla com as informações disponíveis. 

    ################ COMPLETAR

    itens.append((desc, (data, hora, pri, contexto, projeto)))

  return itens


# Datas e horas são armazenadas nos formatos DDMMAAAA e HHMM, mas são exibidas
# como se espera (com os separadores apropridados). 
#
# Uma extensão possível é listar com base em diversos critérios: (i) atividades com certa prioridade;
# (ii) atividades a ser realizadas em certo contexto; (iii) atividades associadas com
# determinado projeto; (vi) atividades de determinado dia (data específica, hoje ou amanhã). Isso não
# é uma das tarefas básicas do projeto, porém. 
def listar():
  return

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

# Recebe uma lista de tuplas no formato (n, 'item') e ordena os itens de acordo com n
def bubbleSortporChave(lista):
  desordenado = True
  iteracao = len(lista) -1
  while iteracao > 0 and desordenado:
    desordenado = False
    for i in range(iteracao):
      if lista[i][0] > lista[i+1][0]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        desordenado = True
    iteracao -= 1
  # Remove o numero usado para ordenar
  i = 0
  while i < len(lista):
    lista[i] = lista[i][1]
    i += 1
  return lista

def ordenarPorDataHora(itens):
  dataseItens = []
  # Cria uma lista que contém um número inteiro derivado da data, seguindo o modelo YYYYMMAAHHmm
  for lin in itens: # l = (desc, (data, hora, pri, cont, projeto))
    data = str(lin[1][0])
    hora = str(lin[1][1])
    dataHora = dataHoraInt(data, hora)
    item = (dataHora, lin)
    dataseItens.append(item)
  listaOrdenada = bubbleSortPorChave(dataseItens)
  return lstOrdenada

def ordenarPorPrioridade(itens):
  prieItens = []
  for linha in itens:
    pri = linha[1][2]
    if pri == '': # No caso de não haver prioridade será atribuída a menor possível
      letra = 'Z'
    else:
      letra = pri[1].upper() # Extrai apenas a letra de '(L)'
    item = (letra, l)
    prieItens.append(item)
  listaOrdenada = bubbleSortPorChave(prieItens)
  return listaOrdenada

def fazer(num):
  return 

def remover():
  return

# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'. 
def priorizar(num, prioridade):
  return 

def processarComandos(comandos) :
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'a'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
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

processarComandos(sys.argv) # sys.argv = ['agenda.py', 'a', 'Mudar', 'de', 'nome']
