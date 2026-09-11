# Módulo 10 — Tratamento de erros

Desde o módulo 03 este material vem fazendo a mesma promessa:

> Digite uma letra quando o programa pedir um número e veja o que acontece: `ValueError`.
>Por enquanto, combine com o programa: só números. No módulo 10 você vai aprender a tratar isso de verdade.

Chegou a hora. A partir daqui seus programas param de morrer por causa de uma digitação.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Explicar a diferença entre erro de sintaxe e exceção
- [ ] Usar `try` / `except` para capturar um erro sem derrubar o programa
- [ ] Capturar exceções específicas em vez de "qualquer erro"
- [ ] Usar `else` e `finally` e dizer quando cada um serve
- [ ] Combinar `try` com `while` para insistir até a entrada ser válida
- [ ] Reconhecer as cinco exceções mais comuns pelo nome
- [ ] Decidir quando **não** capturar um erro

## Pré-requisitos

[Módulo 09 — Matrizes](../modulo-09-matrizes/) concluído. Na prática, o que mais importa é o
módulo 05: a validação com `while` que você já sabe fazer é metade da solução daqui.

## Conceito

### Duas famílias de erro

Você conviveu com as duas desde o módulo 00, sem separá-las:

| Tipo | Quando aparece | Dá para tratar? |
| --- | --- | --- |
| **Erro de sintaxe** | antes de rodar; o Python nem começa | Não. Você conserta o código. |
| **Exceção** | durante a execução, numa situação específica | **Sim.** É disso que trata este módulo. |

`SyntaxError` é gramática errada. Não há o que tratar. Já `ValueError` só acontece se o usuário
digitar texto onde se esperava número: o código está certo, a situação é que deu errado.

### O problema: validar não resolve tudo

No módulo 05 você aprendeu a insistir:

```python
nota = float(input("Nota: "))
while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Nota: "))
```

Isso protege contra `15`. Mas não protege contra `"abc"`: o programa morre **na primeira linha**,
antes de chegar ao `while`. O `float()` explode antes de haver o que validar.

**Validação cuida do valor. Exceção cuida do tipo.** São problemas diferentes, e você precisa dos
dois.

### `try` / `except`

```python
try:
    idade = int(input("Idade: "))
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Isso não é um número inteiro.")
```

Leia assim: "**tente** fazer isto; **se der** `ValueError`, faça aquilo em vez de morrer".

O que acontece na prática:

- Deu certo? O bloco `except` é ignorado por completo.
- Deu erro? O Python **abandona o resto do `try`** na hora e pula para o `except`.

Esse "abandona o resto" importa: se o erro acontece na primeira de cinco linhas do `try`, as outras
quatro não rodam.

### Capture o erro específico, não qualquer um

```python
except ValueError:          # bom: você sabe o que está tratando
except:                     # ruim: engole TUDO, inclusive o Ctrl+C
```

O `except` pelado captura qualquer coisa, inclusive erros de digitação seus, que passam a sumir em
silêncio em vez de aparecer. Um bug escondido é pior que um programa que quebra.

Se precisar tratar mais de um tipo:

```python
try:
    resultado = int(numerador) / int(denominador)
except ValueError:
    print("Digite apenas números.")
except ZeroDivisionError:
    print("Não dá para dividir por zero.")
```

Cada erro com sua mensagem: é isso que torna o programa utilizável.

### As cinco que você já encontrou

| Exceção | Acontece quando | Você viu no |
| --- | --- | --- |
| `ValueError` | `int("abc")`: o texto não vira número | módulo 03 |
| `ZeroDivisionError` | divisão por zero | módulo 03 |
| `IndexError` | `lista[10]` numa lista de 3 | módulo 06 |
| `TypeError` | `"3" + 5`: tipos incompatíveis | módulo 01 |
| `NameError` | usou variável que não existe | módulo 00 |

Nenhuma é nova. O que muda é que agora você pode **reagir** a elas.

### A receita completa: `try` dentro de `while`

Este é o padrão que você vai repetir pelo resto do curso:

```python
while True:
    try:
        nota = float(input("Nota (0 a 10): "))
    except ValueError:
        print("Digite um número.")
        continue                    # volta ao topo, pede de novo

    if 0 <= nota <= 10:
        break                       # valor bom: sai do laço
    print("A nota deve estar entre 0 e 10.")
```

Repare que ele cobre os **dois** problemas: o `except` pega o tipo errado, o `if` pega o valor fora
da faixa. É a soma do módulo 05 com este.

### `else` e `finally`

```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Não era número.")
else:
    print(f"Deu certo: {numero}")       # só roda se NÃO houve erro
finally:
    print("Isto roda sempre.")          # com ou sem erro
```

- **`else`**: para o código que só faz sentido quando deu certo. Serve para manter o `try` curto,
  com apenas a linha que pode falhar.
- **`finally`**: para limpeza que precisa acontecer de qualquer jeito (fechar arquivo, encerrar
  conexão). Você usará pouco agora; saiba que existe.

### Quando **não** capturar

Tratar exceção não é bom por si só. Este código é pior que o erro original:

```python
try:
    media = soma / quantidade
except ZeroDivisionError:
    media = 0                   # inventou um número
```

Uma turma sem alunos passa a ter média zero, indistinguível de uma turma que tirou zero. O erro foi
escondido, não resolvido.

Duas perguntas antes de escrever um `except`:

1. **Eu sei o que fazer neste caso?** Se a resposta honesta é "não, mas quero que pare de quebrar",
   não capture.
2. **Dá para evitar em vez de capturar?** `if quantidade > 0` é melhor que `except
   ZeroDivisionError`: prevenir lê melhor que remediar.

Use `try` quando o erro depende de algo **fora do seu controle**: o que o usuário digitou, um
arquivo que pode não existir, uma rede que pode cair. Para o que está sob seu controle, use `if`.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_try_except.py](exemplos/01_try_except.py) | o primeiro `try`, e o "abandona o resto" |
| [exemplos/02_excecoes_comuns.py](exemplos/02_excecoes_comuns.py) | as cinco mais frequentes, provocadas de propósito |
| [exemplos/03_entrada_robusta.py](exemplos/03_entrada_robusta.py) | `try` + `while`: a receita completa |
| [exemplos/04_else_finally.py](exemplos/04_else_finally.py) | `else`, `finally` e quando não capturar |

Para rodar qualquer um deles:

```bash
cd modulo-10-tratamento-de-erros/exemplos
python 01_try_except.py
```

## Exercícios

1. [EXERCICIO-01-entrada-a-prova-de-tudo.md](exercicios/EXERCICIO-01-entrada-a-prova-de-tudo.md) (nível 1): funções de leitura que não quebram.
2. [EXERCICIO-02-calculadora-robusta.md](exercicios/EXERCICIO-02-calculadora-robusta.md) (nível 2): a calculadora do módulo 04, agora inquebrável.
3. [EXERCICIO-03-auditoria-de-erros.md](exercicios/EXERCICIO-03-auditoria-de-erros.md) (nível 3): decidir onde tratar, onde prevenir e onde deixar quebrar.

## Auto-avaliação

- [ ] Sei explicar por que validar com `while` não protege contra `"abc"`
- [ ] Escrevo `except ValueError` em vez de `except` pelado, e sei por quê
- [ ] Sei que o `try` abandona as linhas restantes quando dá erro
- [ ] Escrevo a receita `try` dentro de `while` sem consultar o README
- [ ] Sei dar um exemplo de erro que **não** deveria ser capturado
- [ ] Sei quando `if` é melhor que `try`

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `except` pelado escondendo bugs | capture o tipo específico: `except ValueError` |
| O `try` engloba o programa inteiro | deixe no `try` só a linha que pode falhar; o resto vai no `else` |
| `except` que só dá `pass` | o erro some sem ninguém saber; no mínimo, avise |
| Capturar e inventar um valor padrão | esconde o problema; pergunte se você sabe mesmo o que fazer |
| Loop infinito no `try`/`while` | faltou o `continue` ou o `break`; confira os dois caminhos |
| `SyntaxError` dentro de `try` | não dá para capturar: o Python nem chega a rodar o arquivo |
| Tratar `ZeroDivisionError` que um `if` evitaria | prevenir lê melhor que remediar |
| `except ValueError` não pega o erro | confira o tipo real na mensagem; pode ser `TypeError` |

---

Anterior: [Módulo 09 — Matrizes](../modulo-09-matrizes/) | Próximo: [Módulo 11 — Algoritmos de ordenação](../modulo-11-algoritmos-de-ordenacao/)
