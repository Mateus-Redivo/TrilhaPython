# 01 Sistema de Biblioteca Pessoal (Python)

## Contexto
Sua biblioteca pessoal cresceu e ficou difícil lembrar quais livros você já leu e quais ainda faltam. O grupo vai construir um sistema de linha de comando para resolver isso, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada livro guarda
Título (obrigatório, até 150 caracteres), autor (obrigatório, até 100 caracteres), gênero (opcional, até 50 caracteres), número de páginas (opcional, não pode ser negativo) e se já foi lido (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de títulos, uma de autores, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda um livro completo com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se título ou autor ficarem vazios. Ao listar, mostre todos os livros numerados, indicando se cada um já foi lido. Marcar como lido é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantos livros existem no total, quantos já foram lidos e quantos ainda faltam ler.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (no número de páginas), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido um livro válido.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de um livro?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido no número de páginas?
- [ ] Testou marcar um livro como lido e ver isso refletido na listagem?
- [ ] Testou remover o único livro da lista?

## Desafios extras (opcional)
- Permitir buscar um livro pelo título, em vez de só pelo número da lista.
- Ordenar a listagem por título ou por autor.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
