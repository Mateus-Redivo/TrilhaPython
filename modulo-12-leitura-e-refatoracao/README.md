# Módulo 12 — Leitura e refatoração

Você passou onze módulos aprendendo a **escrever** código. Na vida profissional, você vai gastar
muito mais tempo **lendo**: código dos outros, e código seu de seis meses atrás, que dá no mesmo.

Este módulo é sobre as duas habilidades que decorrem disso: entender um código que você não
escreveu, e melhorá-lo **sem quebrá-lo**.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Ler um código ruim e descrever o que ele faz, sem executá-lo
- [ ] Nomear os sinais de código que pede refatoração
- [ ] Trocar números mágicos por constantes nomeadas, no topo do arquivo
- [ ] Ligar cada sinal ao princípio que ele fere (DRY, KISS, SRP, YAGNI)
- [ ] Refatorar preservando comportamento, e provar que preservou
- [ ] Explicar por que refatorar e corrigir bugs não devem andar juntos
- [ ] Escrever comentários que envelhecem bem
- [ ] Decidir quando **não** vale a pena refatorar

## Pré-requisitos

[Módulo 11 — Ordenação](../modulo-11-algoritmos-de-ordenacao/) concluído. Na prática, este módulo
usa tudo: você não consegue melhorar um código sem entender listas, laços, condicionais e funções.

## Conceito

### O que é refatorar

> **Refatorar é mudar a estrutura do código sem mudar o que ele faz.**

As duas metades importam igualmente. Se o código não melhorou, você perdeu tempo. Se o
comportamento mudou, você não refatorou: introduziu uma alteração, possivelmente um bug.

Isso leva à regra mais importante do módulo:

> **Nunca refatore e conserte na mesma passada.**

Se você mexe na estrutura e no comportamento ao mesmo tempo e algo quebra, não há como saber qual
das duas mudanças causou. Refatore primeiro, com a saída idêntica; conserte depois, num passo
separado.

### Como se prova que o comportamento não mudou

Não se prova por leitura. Prova-se comparando saídas:

```bash
python versao_antiga.py > antiga.txt
python versao_nova.py > nova.txt
diff antiga.txt nova.txt
```

`diff` sem saída significa arquivos idênticos. No Windows sem `diff`, use `fc antiga.txt nova.txt`.

Você já fez isso no módulo 08, no exercício do monólito. Aqui vira método.

### Os sinais de que um código pede refatoração

| Sinal | O que indica |
| --- | --- |
| Nomes de uma letra (`d`, `p`, `tx`) | ninguém sabe o que a variável guarda sem rastrear o código |
| Função gigante | ela faz coisas demais; cada bloco quer virar uma função |
| Código repetido | mudar a regra exige achar todas as cópias |
| Indentação profunda | três níveis de `if` dentro de `for` dentro de `if` |
| Números soltos (`0.1`, `100`, `46`), os **números mágicos** | ninguém sabe de onde vieram nem o que significam |
| Comentário explicando *o que* a linha faz | se precisa explicar, o nome está ruim |
| Precisa de comentário para separar blocos | cada bloco quer ser uma função |

Nenhum é erro. Todos são **atrito**: o código funciona, mas custa caro para entender e mudar.

### Números mágicos

Um **número mágico** é um valor escrito direto no código, sem nome nenhum que diga o que ele
significa. Quem lê `valor * 1.15` precisa adivinhar: é imposto? comissão? margem? E, se a regra
mudar, é preciso caçar cada `1.15` espalhado pelo arquivo, separando os que significam a regra dos
que são só coincidência.

```python
# Antes: o que são 1.15, 1000 e 50?
def calcular_total(valores):
    total = 0
    for valor in valores:
        if valor < 1000:
            total = total + valor * 1.15
        else:
            total = total + valor * 1.15 + 50
    return total
```

```python
# Depois: constantes no topo do arquivo, com nomes que dizem o que são
FATOR_IMPOSTO = 1.15        # imposto de 15% sobre cada item
LIMITE_TAXA_FIXA = 1000     # a partir deste valor, cobra-se a taxa fixa
TAXA_FIXA = 50              # em reais


def calcular_total(valores):
    total = 0
    for valor in valores:
        if valor < LIMITE_TAXA_FIXA:
            total = total + valor * FATOR_IMPOSTO
        else:
            total = total + valor * FATOR_IMPOSTO + TAXA_FIXA
    return total
```

As duas versões devolvem o mesmo valor para qualquer lista: é refatoração. E agora a regra do
imposto está **num lugar só**: mudar de 15% para 18% é editar uma linha.

**A regra, em quatro passos:**

1. **Ache o número e faça a pergunta-teste:** *alguém que não escreveu este código sabe o que esse
   número significa e de onde ele veio?* Se não, é mágico.
2. **Dê um nome que diga o que ele significa**, e não o valor: `PERCENTUAL_DESCONTO`, e não
   `ZERO_VIRGULA_UM`.
3. **Declare a constante no topo do arquivo**, antes das funções, em MAIÚSCULAS com underscore (a
   convenção do módulo 01). Assim todas as regras do programa ficam juntas, à vista, num lugar só.
4. **Troque cada ocorrência pelo nome** e rode a prova: o valor é o mesmo, então a saída tem de ser
   idêntica.

Três observações:

- **Nem todo número é mágico.** O `0` que inicia um acumulador, o `1` de `contador + 1` e o `2` de
  `numero % 2 == 0` são óbvios, e dar nome a eles piora a leitura. O mesmo vale ao contrário: **textos
  soltos que se repetem**, como `"Aprovado"` escrito em cinco lugares, também viram constante. É um
  dos requisitos do [módulo 14](../modulo-14-projeto-integrador/).
- **Ler uma constante dentro de uma função não precisa de `global`.** O `global` do módulo 08 só é
  necessário para **reatribuir** uma variável de fora. Como a constante não muda, qualquer função
  pode usá-la direto.
- **A constante pode ter um comentário, e deve:** o nome diz o **que** é, o comentário diz o
  **porquê** ou a unidade (`# em reais`, `# regra do contrato`). É o comentário que envelhece bem,
  descrito mais adiante.

### Os princípios por trás dos sinais

Cada linha da tabela acima é um **sintoma**. Quem trabalha com código chama esses sintomas de
*code smells*, "cheiros de código": você sente que algo está errado antes de saber dizer o quê. O
que explica **por que** o sintoma incomoda é um **princípio**, e o princípio ajuda a escolher o
que fazer:

| Princípio | Em uma frase | Sinal que denuncia | O que fazer |
| --- | --- | --- | --- |
| **DRY** (*Don't Repeat Yourself*) | cada regra mora num lugar só | código repetido; o mesmo número solto em vários lugares | extrair função, laço ou constante |
| **KISS** (*Keep It Simple*) | entre duas soluções que funcionam, fique com a mais simples | indentação profunda; `if` que só devolve `True` ou `False` | achatar; devolver a própria condição |
| **SRP** (*Single Responsibility*) | uma função faz uma coisa, e o nome diz qual | função gigante; função que lê, calcula e imprime | separar em funções |
| **YAGNI** (*You Aren't Gonna Need It*) | não escreva o que ninguém pediu | parâmetro que nenhuma chamada usa; código que nunca roda | remover, depois de conferir |
| **Nomes que dizem a intenção** | o nome diz o que a coisa é | nomes de uma letra; comentário que explica o *quê* | renomear |

O SRP você já usou sem saber, no módulo 08: *quem calcula devolve, quem mostra imprime*.

```python
# Antes: lê, calcula e imprime na mesma função
def boletim():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    print(f"Média: {media:.2f}")


# Depois: cada função tem um motivo só para mudar
def ler_nota(mensagem):
    return float(input(mensagem))


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def mostrar_media(media):
    print(f"Média: {media:.2f}")


def boletim():
    n1 = ler_nota("Nota 1: ")
    n2 = ler_nota("Nota 2: ")
    mostrar_media(calcular_media(n1, n2))
```

Com as mesmas entradas, as duas versões escrevem exatamente a mesma coisa na tela: é refatoração.
E, se amanhã a média tiver de sair num arquivo, só `mostrar_media` muda.

**Princípios são perguntas, não leis.** Aplicados sem juízo, pioram o código:

- **DRY exagerado.** Se a nota máxima é `10` e o limite de tentativas de senha também é `10`, uma
  constante `DEZ = 10` para os dois é um erro: são duas regras diferentes, que só *coincidem* no
  valor, e mudam por motivos diferentes. Duplicação por coincidência não precisa ser desfeita.
- **KISS não é "curto".** Uma linha cheia de `sum(...)` e `max(...)` pode ser mais difícil de ler que
  cinco linhas com um laço.
- **YAGNI não é "dispenso a validação".** Ele vale para recurso que **ninguém pediu**, nunca para
  requisito. E apagar o que "ninguém usa" só é refatoração **depois** de procurar todas as
  chamadas.

Uma observação sobre o nome: SRP é a primeira letra do conjunto de cinco princípios chamado
**SOLID**. As outras quatro (O, L, I, D) falam de classes e de orientação a objetos, que ficam
além desta trilha. Aqui o SRP vale para **funções**.

### O que a refatoração não é

- **Não é reescrever do zero.** Reescrever joga fora todas as correções silenciosas que o código
  acumulou, inclusive as que ninguém lembra por que existem.
- **Não é deixar mais curto.** Menos linhas nem sempre é mais claro.
- **Não é adicionar recursos.** Isso é outra tarefa, em outro commit.

### O caso dos cinco pares

A pasta `exemplos/` tem cinco programas em duas versões: `_antes.py` e `_depois.py`. Eles vieram do
material antigo deste repositório e são reais, não foram fabricados para a aula.

Rodando o `diff` nos cinco pares, o resultado surpreende:

| Par | Saída idêntica? |
| --- | --- |
| 01 cálculo de preços | Sim |
| 02 processamento de clientes | **Não** |
| 03 cálculo de seguro | Sim |
| 04 status de pets | **Não** |
| 05 notas de estudantes | **Não** |

Três dos cinco mudaram a saída. **Isso significa que não foram refatorações?**

Não necessariamente, e é aí que o módulo fica interessante. Olhando de perto:

- No **05**, a função devolve exatamente `50.0` nas duas versões. O que mudou foi o `print` final,
  que passou a usar `:.2f` e exibe `50.00`. O **cálculo** é idêntico; a **apresentação** mudou.
- No **04**, o valor também é o mesmo (`30.05`). Mudou o texto do rótulo.
- No **02**, a versão nova acrescentou casos de teste que não existiam antes.

Ou seja: as **funções** foram refatoradas de verdade. O que mudou foi o bloco de demonstração no fim
do arquivo, que não é o programa, é o teste dele.

Isso levanta a pergunta que você vai levar para o resto da carreira: **o que exatamente conta como
"comportamento"?** A resposta prática é: o que o usuário do seu código observa. Se ele chama uma
função, o comportamento é o valor devolvido. Se ele roda um programa, é a saída na tela.

### Comentários que envelhecem bem

```python
# Ruim: explica o QUE, e vira mentira quando alguém mexe na linha
total = preco * 1.1        # multiplica o preço por 1.1

# Bom: explica o PORQUÊ, e continua verdadeiro
total = preco * 1.1        # 10% de taxa de serviço, definida em contrato
```

O melhor comentário costuma ser um nome:

```python
TAXA_DE_SERVICO = 1.1
total = preco * TAXA_DE_SERVICO
```

Agora não é preciso comentário nenhum. **Nome bom é comentário que não apodrece.**

Para os marcadores padronizados (`TODO`, `FIXME`, `NOTE`…), veja o
[guia de comentários](../material-apoio/guia-de-comentarios.md).

### Quando não refatorar

- **Código que você não entende ainda.** Entenda primeiro; mexer no escuro é como andar de olhos
  fechados.
- **Código sem forma de testar.** Sem comparar a saída, você não tem como saber se quebrou.
- **Código que ninguém mais toca.** Se funciona e nunca muda, o atrito não custa nada.
- **Na véspera da entrega.** Refatoração é investimento; investimento tem hora.

## Exemplos guiados

Cinco pares reais, cada um com o código original e a versão melhorada:

| Par | O que o "antes" tem de ruim |
| --- | --- |
| [01_calculo_precos](exemplos/01_calculo_precos_antes.py) / [depois](exemplos/01_calculo_precos_depois.py) | nomes de uma letra, função recursiva ilegível |
| [02_processamento_clientes](exemplos/02_processamento_clientes_antes.py) / [depois](exemplos/02_processamento_clientes_depois.py) | condicionais aninhadas fundas |
| [03_calculo_seguro](exemplos/03_calculo_seguro_antes.py) / [depois](exemplos/03_calculo_seguro_depois.py) | números mágicos por toda parte |
| [04_status_pets](exemplos/04_status_pets_antes.py) / [depois](exemplos/04_status_pets_depois.py) | uma função fazendo cinco coisas |
| [05_notas_estudantes](exemplos/05_notas_estudantes_antes.py) / [depois](exemplos/05_notas_estudantes_depois.py) | parâmetros crípticos (`e`, `c`, `p`, `b`, `d`) |

Para comparar um par:

```bash
cd modulo-12-leitura-e-refatoracao/exemplos
python 05_notas_estudantes_antes.py
python 05_notas_estudantes_depois.py
```

Leia o `_antes` **primeiro**, e tente descrever o que ele faz antes de abrir o `_depois`. É
desconfortável de propósito: é assim que se chega num código na vida real.

## Exercícios

1. [EXERCICIO-01-lendo-codigo-alheio.md](exercicios/EXERCICIO-01-lendo-codigo-alheio.md) (nível 1): descrever o que um código faz sem rodá-lo.
2. [EXERCICIO-02-refatorando-com-prova.md](exercicios/EXERCICIO-02-refatorando-com-prova.md) (nível 2): refatorar e provar que a saída não mudou.
3. [EXERCICIO-03-auditoria-de-refatoracao.md](exercicios/EXERCICIO-03-auditoria-de-refatoracao.md) (nível 3): julgar refatorações alheias, incluindo as deste módulo.

## Auto-avaliação

- [ ] Sei definir refatoração citando as duas metades da definição
- [ ] Sei provar que uma refatoração preservou o comportamento
- [ ] Sei por que refatorar e corrigir não devem andar juntos
- [ ] Reconheço pelo menos cinco sinais de código que pede refatoração
- [ ] Sei dizer o que é um número mágico e onde a constante que o substitui deve ficar
- [ ] Sei ligar cada sinal ao princípio que ele fere (DRY, KISS, SRP, YAGNI)
- [ ] Sei dar um exemplo de princípio aplicado com exagero
- [ ] Escrevo comentários que explicam o porquê
- [ ] Sei dar um exemplo de código que **não** vale a pena refatorar

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| Refatorar e corrigir junto | se quebrar, não há como saber qual mudança causou |
| "Melhorei" sem comparar a saída | sem prova, é só esperança |
| Reescrever do zero | joga fora as correções que ninguém lembra por que existem |
| Encurtar em vez de esclarecer | uma linha densa pode ser pior que cinco claras |
| Renomear tudo de uma vez | mudanças grandes escondem o erro; vá em passos pequenos |
| Comentar o óbvio | `# soma 1 ao contador` não ajuda ninguém |
| Refatorar código que você não entendeu | entenda primeiro, sempre |
| Achar que menos funções é mais simples | uma função de 200 linhas não é "simples", é indivisível |
| Constante com nome que repete o valor (`QUINZE = 15`) | trocou um número mágico por um nome mágico; o nome tem de dizer o que o número **significa** (`FATOR_IMPOSTO`) |
| Criar a constante mas deixar o número solto em outro ponto | a regra continua em dois lugares; procure todas as ocorrências antes de dar a troca por feita |
| Juntar duas coisas só porque se parecem (`DEZ = 10`) | repetição por coincidência não é DRY: se uma regra mudar, a outra não deveria mudar junto |
| Apagar o que "ninguém usa" sem procurar | confira todas as chamadas antes; senão não é refatoração, é quebra |

---

Anterior: [Módulo 11 — Algoritmos de ordenação](../modulo-11-algoritmos-de-ordenacao/) | Próximo: [Módulo 13 — Estudo de caso CRUD](../modulo-13-estudo-de-caso-crud/)
