# 03 Sistema de Watchlist de Filmes e Séries (Python)

## Contexto
A lista de filmes e séries para assistir só cresce, e fica fácil perder o controle do que você já viu, do que ainda falta e do que valeu a pena. O grupo vai construir um sistema de linha de comando para organizar isso, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada título guarda
Título (obrigatório, até 150 caracteres), gênero (opcional, até 50 caracteres), plataforma (opcional, até 50 caracteres), nota de 0 a 10 (opcional) e se já foi assistido (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de títulos, uma de gêneros, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda um título completo com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se o título ficar vazio. Ao listar, mostre todos os títulos numerados, indicando quais já foram assistidos. Marcar como assistido é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantos títulos existem no total, quantos já foram assistidos e quantos ainda faltam.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (na nota), aceitar uma nota fora da faixa de 0 a 10, tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido um título válido.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de um título?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar uma nota fora da faixa de 0 a 10?
- [ ] Testou marcar um título como assistido e ver isso refletido na listagem?
- [ ] Testou remover o único título da lista?

## Desafios extras (opcional)
- Permitir buscar um título pelo nome, em vez de só pelo número da lista.
- Ordenar a listagem pela nota, do maior para o menor.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
