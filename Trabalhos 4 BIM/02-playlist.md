# 02 Sistema de Playlist Musical (Python)

## Contexto
Sua playlist foi crescendo e ficou difícil lembrar quais músicas você mais gosta no meio de tantas outras. O grupo vai construir um sistema de linha de comando para organizar isso, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada música guarda
Título (obrigatório, até 150 caracteres), artista (obrigatório, até 100 caracteres), álbum (opcional, até 100 caracteres), duração em segundos (opcional, não pode ser negativa) e se é favorita (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de títulos, uma de artistas, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda uma música completa com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se título ou artista ficarem vazios. Ao listar, mostre todas as músicas numeradas, indicando quais são favoritas. Favoritar/desfavoritar é uma ação separada que apenas alterna o valor atual, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantas músicas existem no total, quantas são favoritas e quantas não são.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (na duração), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido uma música válida.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de uma música?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido na duração?
- [ ] Testou favoritar e depois desfavoritar a mesma música?
- [ ] Testou remover a única música da lista?

## Desafios extras (opcional)
- Permitir buscar uma música pelo título ou pelo artista, em vez de só pelo número da lista.
- Ordenar a listagem por artista ou por duração.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
