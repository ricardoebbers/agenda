# agenda
## Projeto da cadeira de Programação 01 do curso de Sistemas de Informação da UFPE

## Resumo do programa:
  O agenda.py é um organizador de afazeres, eventos e responsabilidades usável à partir da linha de comando do Windows, Linux (testados) e IOS (não testado). Com o agenda.py é possível adicionar tarefas, listar de forma organizada e visual, marcar tarefas como feitas (e salvar num arquivo separado) ou removê-las.

## Objetivo geral do projeto:
  Desenvolver um sistema não-trivial em Python;
## Objetivos específicos:

a. Praticar a escrita de funções e programas com foco em:
 1. Strings;
 2. Vetores;
 3. Listas;
 4. Tuplas;
 5. Dicionários;
 6. Arquivos.

b. Entender completamente o que é pedido no projeto;

c. Anotar dúvidas para sanar em sala de aula.

## Metodologia:
  Realizar todas as tarefas solicitadas no arquivo projeto.pdf.
  - [x] **Tarefa 0:** ler o documento com bastante cuidado.
  
  - [x] **Tarefa 1:** Obtenha os arquivos todo.txt e agenda.py a partir do endereço https://sites.google.com/a/cin.ufpe.br/if968si/projeto
  
  - [x] **Tarefa 2:** Crie manualmente um arquivo todo.txt e inclua nele diversos compromissos como os apresentados nesta seção. Invente novos compromissos, porém, para ter um arquivo que lhe ajude a testar todas as funcionalidades do programa que você vai construir. Seu arquivo também deve incluir algumas atividades fora do formato especificado, por exemplo, com uma data com menos que 8 dígitos, para verificar como seu programa se comporta. O número total de atividades desse arquivo deve ser maior ou igual a 20 e deve contemplar todas as funcionalidades da aplicação.
  
  - [x] **Tarefa 3:** Complete a implementação da função horaValida() . Essa função recebe um string e verifica se ele tem exatamente quatro caracteres, se tão todos dígitos, se os dois primeiros formam um número entre 00 e 23 e se os dois últimos formam um número inteiro entre 00 e 59. Se tudo isso for verdade, ela devolve True. Caso contrário, False. O arquivo já inclui uma função auxiliar para verificar se todos os caracteres de um string são dígitos.
  
  - [x] **Tarefa 4:** Implemente a função dataValida() . Essa função recebe um string e verifica se ele tem exatamente oito caracteres, se tão todos dígitos e se os dois primeiros correspondem a um dia válido, se o terceiro e o quarto correspondem a um mês válido e se os quatro últimos correspondem a um ano válido. Sua função deve checar também se o dia e o mês fazem sentido juntos. Além de verificar se o mês é um número entre 1 e 12, dataValida() deve checar se o dia poderia ocorrer naquele mês, por exemplo, ela deve devolver False caso o dia seja 31 mas o mês seja 04, que tem apenas 30 dias. O ano pode ser qualquer número de 4 dígitos. Para fevereiro, considere que pode haver até 29 dias, sem se preocupar se o ano é bissexto ou não. Se todas as verificações passarem, a função devolve True. Caso contrário, False.
  
  - [x] **Tarefa 5:** Implemente a função projetoValido(). Essa função recebe um string e verifica se ele tem pelo menos dois caracteres e se o primeiro é ‘+’. Devolve True se as verificações passarem e False caso contrário.
  
  - [x] **Tarefa 6:** Implemente a função contextoValido(). Essa função recebe um string e verifica se ele tem pelo menos dois caracteres e se o primeiro é ‘@’. Devolve True se as verificações passarem e False caso contrário.
  
  - [x] **Tarefa 7:** Implemente a função prioridadeValida(). Essa função recebe um string e verifica se ele tem exatamente três caracteres, se o primeiro é ‘(’, se o terceiro é ‘)’ e se o segundo é uma letra entre A e Z. A função deve funcionar tanto para letras minúsculas quanto maiúsculas. Devolve True se as verificações passarem e False caso contrário.
  
  - [x] **Tarefa 8:** Complete a implementação da função organizar(). Como dito antes, essa função recebe uma lista de strings representando atividades e devolve uma lista de tuplas com as informações dessas atividades organizadas.
  
  - [x] **Tarefa 9:** Complete a implementação da função adicionar(), que adiciona um compromisso à agenda. Um compromisso tem no mínimo uma descrição. Adicionalmente, pode ter, em caráter opcional, uma data, um horário, um contexto e um projeto. Esses itens opcionais são os elementos da tupla extras, o segundo parâmetro da função. Veja os comentários do código para saber como essa tupla é organizada. Todos os elementos dessa tupla precisam ser validados (com as funções definidas nas tarefas anteriores). Qualquer elemento da tupla que não passe pela validação deve ser ignorado.
  
  - [x] **Tarefa 10:** Modifique a função processarComandos() para que, ao receber o comando l, invoque a função listar().
  
  - [x] **Tarefa 11:** Modifique a função listar() para ler o conteúdo do arquivo todo.txt em uma lista de strings e organizar esses strings em uma lista de tuplas, usando a função organizar().
  
  - [x] **Tarefa 12:** Construa uma função ordenarPorDataHora() que, dada uma lista de itens como a produzida por organizar(), com os itens já ordenados por prioridade, devolve uma lista que tem os mesmos itens, ordenados com base em suas datas e horas. Quanto mais antiga a data de um item, mais próximo do topo da lista o item deve estar. Itens que não têm data ou hora aparecem sempre no final, sem nenhuma ordem em particular. Modifique a função listar() que faça uso de ordenarPorDataHora().
  
  - [x] **Tarefa 13:** Construa uma função ordenarPorPrioridade() que, dada uma lista de itens como a produzida por organizar(), devolve uma lista que tem os mesmos itens, ordenados com base em suas prioridades, onde itens com prioridades mais altas (e.g., A), aparecem antes daqueles com prioridades mais baixas (e.g., Z). Itens que não têm prioridade aparecem sempre no final, sem qualquer ordem particular. Sua função deve garantir que, se uma lista de itens já estava ordenada por data e hora, essa ordem é mantida para cada prioridade (mas não entre prioridades). Por exemplo, se antes a lista estava ordenada por data e havia nela os seguintes itens:
  * 20052017 (B)
  * 21052017 (A)
  * 22052017 (B)
  
  Após a execução de ordenarPorPrioridade(), a lista passaria a estar ordenada da seguinte maneira:
  * 21052017 (A)
  * 20052017 (B)
  * 22052017 (B)
  
  ou seja, o item com a prioridade A passou a aparecer primeiro mas os itens com prioridade B continuam apresentando a mesma ordem entre si. Modifique a função listar() que faça uso de ordenarPorPrioridade().
  
  - [x] **Tarefa 14:** Modifique a função listar() para que liste as atividades no arquivo todo.txt. Os itens devem ser listados na ordem definida anteriormente, com itens nas prioridades A-D aparecendo em cores e itens com prioridade A também em negrito. Além disso, deve aparecer a numeração dos itens, como explicado antes nesta seção, de modo que possa ser usada pelas funções da próxima seção.
  
  - [x] **Tarefa 15:** Modifique a função processarComandos() para que, ao receber o comando r e o número de uma atividade, invoque a função remover() passando esse número como parâmetro.
  
  - [x] **Tarefa 16:** Construa a função remover() que, dado o número de uma atividade, remove essa atividade do arquivo todo.txt. Se a atividade com esse número não existir, a função deve imprimir uma mensagem de erro.
  
  - [x] **Tarefa 17:** Modifique a função processarComandos() para que, ao receber o comando p e o número de uma atividade, invoque a função priorizar() passando esse número como parâmetro.
  
  - [x] **Tarefa 18:** Construa a função priorizar() que, dados o número N de uma atividade e uma prioridade P, modifica a prioridade dessa atividade N para que se torne P. Se essa atividade já tiver outra prioridade, ela é sobrescrita. Se a atividade não existir, a função deve imprimir uma mensagem de erro.
  
  - [x] **Tarefa 19:** Modifique a função processarComandos() para que, ao receber o comando p e o número de uma atividade, invoque a função priorizar() passando esse número como parâmetro.
  
  - [x] **Tarefa 20:** Construa a função fazer() que, dados o número N de uma atividade, marca essa atividade como feita. Isso significa que a atividade é removida do todo.txt e movida para o done.txt.

  - [x] **Tarefa 21:** Modifique a função processarComandos() para que, ao receber o comando f e o número de uma atividade, invoque a função fazer() passando esse número como parâmetro.
  
