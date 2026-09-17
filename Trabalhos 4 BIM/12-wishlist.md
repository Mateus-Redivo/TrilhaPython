# 12 Sistema de Lista de Desejos (Python)

## Contexto
Aquela lista de coisas que você quer comprar um dia costuma ficar espalhada em anotações soltas. O grupo vai construir um sistema de linha de comando para organizar os itens por prioridade e marcar o que já foi comprado, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada item guarda
Nome (obrigatório, até 150 caracteres), preço (obrigatório, não pode ser negativo), prioridade (opcional, por exemplo "baixa", "média" ou "alta") e se já foi comprado (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de nomes, uma de preços, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda um item completo com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se o nome ficar vazio ou se o preço for negativo. Ao listar, mostre todos os itens numerados, indicando quais já foram comprados. Marcar como comprado é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantos itens existem no total, quantos já foram comprados e quantos ainda faltam.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (no preço), aceitar um preço negativo, tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido um item válido.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de um item?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido ou negativo no preço?
- [ ] Testou marcar um item como comprado e ver isso refletido na listagem?
- [ ] Testou remover o único item da lista?

## Desafios extras (opcional)
- Permitir buscar um item pelo nome, em vez de só pelo número da lista.
- Ordenar a listagem pelo preço ou pela prioridade.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
