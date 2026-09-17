# 06 Sistema de Diário de Treinos (Python)

## Contexto
Sem registrar os treinos, fica difícil lembrar quantas séries e repetições foram feitas em cada exercício, ou até se o treino do dia já foi concluído. O grupo vai construir um sistema de linha de comando para esse controle, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada treino guarda
Exercício (obrigatório, até 100 caracteres), número de séries (obrigatório, não pode ser negativo), número de repetições (obrigatório, não pode ser negativo), grupo muscular (opcional, até 50 caracteres) e se já foi concluído hoje (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de exercícios, uma de séries, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda um treino completo com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se exercício, séries ou repetições ficarem vazios. Ao listar, mostre todos os treinos numerados, indicando quais já foram concluídos hoje. Marcar como concluído é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantos treinos existem no total, quantos já foram concluídos hoje e quantos ainda faltam.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (em séries ou repetições), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido um treino válido.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de um treino?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido em séries ou repetições?
- [ ] Testou marcar um treino como concluído e ver isso refletido na listagem?
- [ ] Testou remover o único treino da lista?

## Desafios extras (opcional)
- Permitir buscar um treino pelo nome do exercício, em vez de só pelo número da lista.
- Ordenar a listagem pelo grupo muscular.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
