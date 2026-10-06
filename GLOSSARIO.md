# Glossário

Termos que aparecem nos módulos, explicados em linguagem simples. Sempre que um README usar uma
palavra que você não reconhece, procure aqui antes de seguir: vocabulário travado atrapalha mais
que conceito difícil.

Os termos estão em ordem alfabética. A coluna *Você vê primeiro em* diz em qual módulo o termo
aparece, para você não se assustar com o que ainda não estudou.

---

## A

**Acumulador**: variável que vai guardando um resultado parcial dentro de um laço. O `soma = 0`
que fica **antes** do `for` e cresce a cada volta é o exemplo clássico. *(Módulo 05)*

**Algoritmo**: a receita: a sequência de passos que resolve um problema. Existe antes do código e
independe da linguagem. Você pode escrever um algoritmo num guardanapo.

**Argumento**: o valor que você **passa** para uma função na hora de chamá-la. Em
`calcular_media(7, 8)`, o `7` e o `8` são argumentos. *(Módulo 08)*

**Atribuição**: dar um valor a uma variável, com um `=` só. `idade = 20` é atribuição.
Não confunda com `==`, que é comparação. *(Módulo 01)*

## B

**Booleano (`bool`)**: o tipo que só tem dois valores possíveis: `True` e `False`. É o que toda
condição de `if` e de `while` produz por baixo dos panos. *(Módulo 01)*

**`break`**: comando que interrompe o laço na hora, mesmo que a condição ainda seja verdadeira.
*(Módulo 05)*

## C

**Code smell** (*cheiro de código*): sinal no código que não é um erro, mas avisa que ele vai custar
caro para ler e mudar: código repetido, nomes de uma letra, número mágico. Quase sempre é a pista
de que algum princípio foi violado. *(Módulo 12)*

**Comentário**: texto que o Python ignora, escrito para humanos. Começa com `#`. Serve para
explicar *por que* o código faz algo, não *o que* ele faz. Isso o código já diz sozinho.

**Concatenar**: grudar duas strings uma na outra: `"bom" + " dia"` vira `"bom dia"`. *(Módulo 07)*

**Condição**: a expressão que o `if` ou o `while` testa e que resulta em `True` ou `False`.
Em `if idade >= 18:`, a condição é `idade >= 18`. *(Módulo 04)*

**Constante**: variável que, por combinação entre programadores, não deve mudar de valor.
Escreve-se em maiúsculas: `NOTA_MINIMA = 6.0`. O Python não impede a mudança; o nome em maiúsculas
é um aviso para quem lê. Serve para dar nome a valores que ficariam soltos no código (veja
*Número mágico*) e fica no topo do arquivo. *(Módulo 12)*

**`continue`**: comando que pula o resto da volta atual do laço e vai direto para a próxima.
*(Módulo 05)*

## D

**Depurar (*debug*)**: investigar por que o programa faz o que faz. A técnica mais simples e mais
subestimada é espalhar `print()` para ver o valor das variáveis em cada ponto.

**Docstring**: texto entre `"""três aspas"""` no topo de um arquivo ou de uma função, explicando o
que aquilo faz. Diferente do comentário, fica acessível ao programa em tempo de execução.

**DRY** (*Don't Repeat Yourself*): princípio que diz que cada regra deve morar num lugar só. Código
copiado e colado, ou o mesmo número escrito em vários pontos, viola o DRY. *(Módulo 12)*

## E

**Escopo**: a região do código onde uma variável existe. Uma variável criada dentro de uma função
morre quando a função termina: ela é **local**. *(Módulo 08)*

**Exceção**: o erro que acontece durante a execução e derruba o programa, como o `ValueError` de
`int("abc")`. Tratar exceções é ensinar o programa a reagir em vez de morrer. *(Módulo 10)*

**Expressão**: qualquer trecho que produz um valor: `2 + 2`, `nota >= 6`, `nome.upper()`.

## F

**f-string**: a forma moderna de montar texto com valores dentro, marcada com `f` antes das aspas:
`f"Olá, {nome}!"`. O que estiver entre chaves é substituído pelo valor. *(Módulo 03)*

**Float (`float`)**: número com casas decimais: `3.14`, `7.0`. Em Python o separador decimal é
**ponto**, não vírgula. *(Módulo 01)*

**Função**: bloco de código com nome, que você escreve uma vez e chama quantas quiser. Recebe
entradas (parâmetros) e normalmente devolve uma saída (retorno). *(Módulo 08)*

## I

**Indentação**: os espaços no começo da linha que dizem ao Python o que está *dentro* de quê. Em
outras linguagens é estética; em Python é **sintaxe**. Padrão: 4 espaços por nível.

**Índice**: a posição de um item dentro de uma lista ou string. **Começa em zero**: o primeiro
item é `lista[0]`. Essa é a fonte de metade dos erros de quem está começando. *(Módulo 06)*

**Inteiro (`int`)**: número sem casas decimais: `-3`, `0`, `42`. *(Módulo 01)*

**`input()`**: função que pausa o programa, espera o usuário digitar e devolve o que foi digitado.
Devolve **sempre uma string**, mesmo que o usuário digite um número. *(Módulo 03)*

**Iterar**: percorrer os elementos de uma sequência um por um. É o que o `for` faz. *(Módulo 05)*

## K

**KISS** (*Keep It Simple*): princípio que diz que, entre duas soluções que funcionam, deve-se
escolher a mais simples de ler. Simples não é o mesmo que curto. *(Módulo 12)*

## L

**Laço (*loop*)**: estrutura que repete um bloco de código. Em Python: `while` e `for`.
*(Módulo 05)*

**Laço infinito**: laço que nunca para porque a condição nunca fica falsa. Quase sempre é uma
variável de controle que ninguém atualizou. Mata-se com `Ctrl + C`. *(Módulo 05)*

**Lista**: coleção ordenada e modificável de valores, escrita entre colchetes:
`notas = [8, 7, 10]`. *(Módulo 06)*

## M

**Matriz**: lista de listas, usada para representar tabelas e grades:
`[[1, 2], [3, 4]]`. Acessa-se com dois índices: `matriz[1][0]`. *(Módulo 09)*

**Método**: função que pertence a um objeto e se chama com ponto: `nome.upper()`,
`lista.append(5)`. *(Módulo 06)*

## N

**Número mágico**: número escrito direto no código, sem nome que diga o que significa: o `1.15` em
`valor * 1.15`. A cura é uma constante com nome, declarada no topo do arquivo. *(Módulo 12)*

## O

**Operador aritmético**: `+`, `-`, `*`, `/`, `//` (divisão inteira), `%` (resto), `**` (potência).
*(Módulo 02)*

**Operador de comparação**: `==`, `!=`, `>`, `<`, `>=`, `<=`. Todos produzem `True` ou `False`.
*(Módulo 02)*

**Operador lógico**: `and`, `or`, `not`. Combinam condições. *(Módulo 02)*

## P

**Parâmetro**: o nome que a função dá ao valor que vai receber. Em
`def calcular_media(nota1, nota2):`, `nota1` e `nota2` são parâmetros. Na chamada, os valores que
você passa são os *argumentos*. *(Módulo 08)*

**Princípio (de projeto)**: regra de bolso que explica por que um sinal no código atrapalha e ajuda
a escolher o que fazer. DRY, KISS, SRP e YAGNI são princípios. São perguntas, não leis: aplicados
sem juízo, pioram o código. *(Módulo 12)*

**`print()`**: função que mostra algo na tela. *(Módulo 03)*

## R

**`range()`**: gera uma sequência de números para o `for` percorrer. O limite final é
**exclusivo**: `range(1, 11)` vai de 1 a 10. *(Módulo 05)*

**Refatorar**: reescrever um código para ficar mais claro **sem mudar o que ele faz**. Se o
comportamento mudou, não foi refatoração. *(Módulo 12)*

**Retorno (`return`)**: o valor que a função entrega de volta a quem a chamou. Também encerra a
função na hora. *(Módulo 08)*

## S

**Sentinela**: valor combinado que sinaliza "acabou". No pedido "digite números até digitar 0", o
zero é a sentinela. *(Módulo 05)*

**Sintaxe**: as regras de escrita da linguagem. Erro de sintaxe é erro de gramática: o Python nem
começa a rodar o programa. *(Módulo 01)*

**`snake_case`**: convenção de nome do Python: tudo minúsculo, palavras separadas por underline.
`media_da_turma`, não `MediaDaTurma`.

**SOLID**: conjunto de cinco princípios de projeto. O primeiro, o SRP, vale para funções; os outros
quatro tratam de classes e orientação a objetos, assunto além desta trilha. *(Módulo 12)*

**SRP** (*Single Responsibility Principle*): princípio que diz que uma função deve fazer uma coisa
só, e o nome dela deve dizer qual. Uma função que lê, calcula e imprime tem três motivos para
mudar. *(Módulo 12)*

**String (`str`)**: texto, escrito entre aspas: `"Maria"`, `'python'`. *(Módulo 01)*

## T

**Tipo**: a categoria de um valor: `int`, `float`, `str`, `bool`, `list`. Define quais operações
fazem sentido. Somar dois `int` dá um número; somar duas `str` gruda os textos. *(Módulo 01)*

## V

**Validação**: verificar se o dado que chegou é aceitável antes de usá-lo. "A nota está entre 0 e
10?" é validação. *(Módulo 05)*

**Variável**: um nome que aponta para um valor guardado na memória. Você cria com `=` e pode
trocar o valor quantas vezes quiser. *(Módulo 01)*

**Variável de controle**: a variável que decide quantas voltas o laço dá: o `contador` do `while`,
o `i` do `for`. *(Módulo 05)*

## Y

**YAGNI** (*You Aren't Gonna Need It*): princípio que diz para não escrever o que ninguém pediu:
parâmetros que nenhuma chamada usa, recursos "para o futuro". Vale para recurso especulativo, nunca
para requisito. *(Módulo 12)*

---

Não achou o termo? Ele pode estar no [resumo de sintaxe](material-apoio/resumo-sintaxe.md), que
mostra *como se escreve*, enquanto este glossário explica *o que significa*.
