# Módulo 07 — Strings

Texto é o tipo de dado que mais aparece nos seus programas: nome, cidade, opção de menu, tudo que
vem do `input()`. Até aqui você tratou strings como blocos fechados: imprimia e comparava. Agora
vai **abrir** esse bloco: pegar pedaços, transformar, procurar e dividir.

E vai resolver um problema que já te incomodou: por que `"SIM"` e `"sim"` não são a mesma coisa.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Acessar caracteres por índice e fatiar strings
- [ ] Explicar por que uma string não pode ser alterada no lugar
- [ ] Usar `upper()`, `lower()`, `strip()`, `replace()` e `title()`
- [ ] Comparar textos ignorando maiúsculas e espaços sobrando
- [ ] Buscar com `in`, `find()`, `startswith()` e `endswith()`
- [ ] Quebrar texto em lista com `split()` e juntar com `join()`
- [ ] Percorrer uma string caractere a caractere
- [ ] Verificar o conteúdo de uma string com `isalpha()`, `isdigit()` e afins

## Pré-requisitos

[Módulo 06 — Listas](../modulo-06-listas/) concluído. String e lista são parentes próximas: as duas
são **sequências**, e quase tudo que você aprendeu de índice e fatia funciona igual aqui. O
`split()` inclusive devolve uma lista.

## Conceito

### O problema: o usuário nunca digita do jeito que você espera

```python
resposta = input("Deseja continuar? (sim/nao) ")

if resposta == "sim":
    print("Continuando...")
```

Parece certo. Mas o usuário digita `"Sim"`. Ou `"SIM"`. Ou `" sim"` com um espaço que entrou sem
querer. Nos três casos, seu programa responde que não.

Não é o usuário que está errado. É o programa que está frágil. Este módulo é sobre deixá-lo
robusto.

### String é uma sequência, como a lista

```python
texto = "Python"
#        012345
#       -654321

texto[0]        # "P"
texto[-1]       # "n"
texto[0:6]      # "Python"
texto[:3]       # "Pyt"
len(texto)      # 6
"th" in texto   # True
```

Tudo idêntico ao módulo 06. Se você entendeu índice e fatia lá, já sabe metade deste módulo.

Dá até para percorrer com `for`:

```python
for letra in "Ana":
    print(letra)
```

### A diferença que importa: string não muda

Aqui a semelhança com listas acaba:

```python
notas = [7, 8]
notas[0] = 10           # funciona: lista é mutável

nome = "Ana"
nome[0] = "E"           # TypeError: 'str' object does not support item assignment
```

Strings são **imutáveis**: uma vez criada, aquela sequência de caracteres não muda. Todo método que
"transforma" uma string na verdade **devolve uma nova**:

```python
nome = "ana"
nome.upper()            # devolve "ANA"
print(nome)             # mas nome continua "ana"!

nome = nome.upper()     # é preciso guardar o resultado
print(nome)             # agora sim: "ANA"
```

> Repare que aqui a regra é o **oposto** do que você viu em listas. Lá, `notas.sort()` modificava a
> lista e devolvia `None`: guardar o retorno era o erro. Aqui, `nome.upper()` não modifica nada e
> devolve o resultado: **não** guardar é o erro. A pergunta que resolve os dois casos: "este método
> altera o objeto ou cria um novo?"

### Transformar

| Método | Faz |
| --- | --- |
| `.upper()` | tudo MAIÚSCULO |
| `.lower()` | tudo minúsculo |
| `.title()` | Primeira Letra De Cada Palavra |
| `.capitalize()` | Só a primeira letra da frase |
| `.strip()` | remove espaços das duas pontas |
| `.replace(a, b)` | troca **todas** as ocorrências de `a` por `b` |

### A receita para comparar entrada de usuário

Juntando `.strip()` e `.lower()`, o problema da abertura desaparece:

```python
resposta = input("Deseja continuar? (sim/nao) ").strip().lower()

if resposta == "sim":
    print("Continuando...")
```

Agora `"Sim"`, `"SIM"`, `" sim "` e `"sIm"` funcionam todos. **Adote isso como padrão** para toda
comparação de texto vindo do usuário.

Repare que os métodos foram encadeados: `.strip()` devolve uma string, e essa string recebe
`.lower()`. Lê-se da esquerda para a direita.

### Buscar

```python
frase = "Python é uma linguagem"

"uma" in frase              # True   — o mais simples, e o preferido
frase.find("uma")           # 9      — a posição, ou -1 se não achar
frase.count("a")            # 2      — quantas vezes aparece
frase.startswith("Py")      # True
frase.endswith("gem")       # True
```

Use `in` quando você só quer saber **se** existe; `find()` quando precisa saber **onde**.

> Cuidado com `find()`: quando não encontra, ele devolve `-1`, não um erro. E `-1` é um índice
> válido em Python (o último caractere), por isso nunca use o resultado direto sem testar.

### Dividir e juntar

```python
frase = "Python é uma linguagem"

palavras = frase.split()            # ['Python', 'é', 'uma', 'linguagem']
data = "30/07/2026".split("/")      # ['30', '07', '2026']

" ".join(palavras)                  # "Python é uma linguagem"
"-".join(["30", "07", "2026"])      # "30-07-2026"
```

`split()` devolve uma **lista**: é a ponte entre este módulo e o anterior. E `join()` é o caminho
de volta. A escrita do `join` estranha à primeira vista: o separador vem primeiro, e a lista vai
dentro dos parênteses.

### Comparação alfabética e a cilada das maiúsculas

```python
"Ana" < "Bruno"     # True  — como no dicionário
"Zebra" < "ana"     # True  — surpresa!
```

O segundo caso já apareceu no módulo 02. O motivo é que a comparação usa a tabela de caracteres, e
nela **todas as maiúsculas vêm antes de todas as minúsculas**. `"Z"` é 90; `"a"` é 97.

A solução é a mesma receita de sempre:

```python
"Zebra".lower() < "ana".lower()     # False — agora é a ordem esperada
```

### Perguntar o que tem dentro da string

Além de transformar e buscar, dá para **perguntar** para a string (ou para um caractere dela) que
tipo de conteúdo ela tem. São métodos que devolvem `True` ou `False`, e todos terminam em `is`:

| Método | Pergunta |
| --- | --- |
| `.isalpha()` | é só letra? |
| `.isdigit()` | é só dígito (0-9)? |
| `.isnumeric()` | é numérico? (inclui `.isdigit()` e mais alguns casos, como frações) |
| `.isalnum()` | é letra ou dígito, sem símbolo nem espaço? |
| `.isspace()` | é só espaço em branco? |
| `.isupper()` / `.islower()` | está tudo em maiúsculas / minúsculas? |

```python
"maria".isalpha()      # True
"maria123".isalpha()   # False — tem dígito

"45999991234".isdigit()   # True
"45,5".isdigit()          # False — vírgula não é dígito
"-10".isdigit()           # False — sinal também não conta
```

Repare que, assim como `upper()` e `lower()`, esses métodos podem ser chamados tanto na string
inteira quanto em cada caractere dela — é assim que se conta letras e dígitos separadamente:

```python
frase = "Python 2026"
letras = 0
digitos = 0

for caractere in frase:
    if caractere.isalpha():
        letras += 1
    elif caractere.isdigit():
        digitos += 1
```

Use `.isdigit()` para conferir que uma entrada numérica (telefone, CEP, código) só tem números
antes de converter com `int()` — é a forma de evitar um `ValueError` sem ainda usar `try/except`
(módulo 10). E use `.isalpha()` quando quiser separar letras de números, espaços e pontuação, como
no desafio do primeiro exercício deste módulo.

> `isdigit()` não aceita sinal (`-10`) nem separador decimal (`3.14`): para esses casos, o
> `int()`/`float()` direto dentro de um `try/except` é o caminho — assunto do módulo 10.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_indices_e_fatias.py](exemplos/01_indices_e_fatias.py) | string como sequência, e a imutabilidade |
| [exemplos/02_transformando.py](exemplos/02_transformando.py) | `upper`, `lower`, `strip`, `replace` e o retorno que precisa ser guardado |
| [exemplos/03_comparando.py](exemplos/03_comparando.py) | a receita `.strip().lower()` para entrada de usuário |
| [exemplos/04_buscando_e_dividindo.py](exemplos/04_buscando_e_dividindo.py) | `in`, `find`, `count`, `split` e `join` |

Para rodar qualquer um deles:

```bash
cd modulo-07-strings/exemplos
python 01_indices_e_fatias.py
```

## Exercícios

1. [EXERCICIO-01-analisador-de-frases.md](exercicios/EXERCICIO-01-analisador-de-frases.md)
   (nível 1): contar, transformar e dividir.
2. [EXERCICIO-02-validador-de-cadastro.md](exercicios/EXERCICIO-02-validador-de-cadastro.md)
   (nível 2): limpar e conferir dados digitados.
3. [EXERCICIO-03-cifra-de-cesar.md](exercicios/EXERCICIO-03-cifra-de-cesar.md)
   (nível 3): criptografia com `ord`, `chr` e aritmética modular.

## Auto-avaliação

- [ ] Sei por que `nome[0] = "E"` não funciona
- [ ] Sei por que `nome.upper()` sozinho não muda nada
- [ ] Escrevo `.strip().lower()` automaticamente ao comparar entrada do usuário
- [ ] Sei a diferença entre usar `in` e usar `find()`
- [ ] Transformo uma frase em lista de palavras e de volta em frase
- [ ] Sei explicar por que `"Zebra" < "ana"` é `True`
- [ ] Sei por que `"3.14".isdigit()` é `False`

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `TypeError: 'str' object does not support item assignment` | string é imutável; crie uma nova com `replace()` ou fatias |
| `nome.upper()` "não funciona" | funciona, mas devolve; é preciso escrever `nome = nome.upper()` |
| `if resposta == "sim"` falha com `"Sim"` | compare com `.strip().lower()` dos dois lados |
| `find()` devolvendo `-1` usado como índice | `-1` é o último caractere; teste `if posicao != -1` antes |
| `replace()` trocando mais do que se queria | ele troca **todas** as ocorrências, não só a primeira |
| `IndexError: string index out of range` | mesma regra da lista: o último índice é `len(texto) - 1` |
| `split()` com resultado inesperado | sem argumento ele divide por espaços; com `","` divide por vírgula |
| `join()` com lista de números | `join` só junta textos; converta com `str()` antes |
| `"-10".isdigit()` ou `"3.14".isdigit()` é `False` | `isdigit()` não aceita sinal nem ponto decimal; serve só para inteiros positivos |

---

Anterior: [Módulo 06 — Listas](../modulo-06-listas/) | Próximo: [Módulo 08 — Funções](../modulo-08-funcoes/)
