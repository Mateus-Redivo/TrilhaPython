# 07 Sistema de Receitas Culinárias (Python)

## Contexto
Toda receita boa que você encontra por aí acaba se perdendo entre anotações soltas e prints de celular. O grupo vai construir um sistema de linha de comando para guardar as receitas favoritas em um só lugar, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada receita guarda
Nome (obrigatório, até 100 caracteres), ingredientes (obrigatório, texto livre ou lista separada por vírgula), tempo de preparo em minutos (opcional, não pode ser negativo), dificuldade (opcional, por exemplo "fácil", "médio" ou "difícil") e se é favorita (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de nomes, uma de ingredientes, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda uma receita completa com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se nome ou ingredientes ficarem vazios. Ao listar, mostre todas as receitas numeradas, indicando quais são favoritas. Favoritar/desfavoritar é uma ação separada que apenas alterna o valor atual, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantas receitas existem no total, quantas são favoritas e quantas não são.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (no tempo de preparo), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido uma receita válida.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de uma receita?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido no tempo de preparo?
- [ ] Testou favoritar e depois desfavoritar a mesma receita?
- [ ] Testou remover a única receita da lista?

## Desafios extras (opcional)
- Permitir buscar uma receita pelo nome, em vez de só pelo número da lista.
- Ordenar a listagem pelo tempo de preparo.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
