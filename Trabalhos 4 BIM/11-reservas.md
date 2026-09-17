# 11 Sistema de Reserva de Salas e Equipamentos (Python)

## Contexto
Uma escola ou empresa com várias salas e equipamentos precisa de um jeito organizado de saber quem reservou o quê e quando, para evitar que duas pessoas tentem usar o mesmo recurso ao mesmo tempo. O grupo vai construir um sistema de linha de comando para esse controle, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada reserva guarda
Recurso reservado, sala ou equipamento (obrigatório, até 100 caracteres), responsável (obrigatório, até 100 caracteres), data e hora (obrigatório, no formato AAAA-MM-DDTHH:mm), capacidade (opcional, não pode ser negativa) e se já foi confirmada (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de recursos, uma de responsáveis, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda uma reserva completa com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se recurso, responsável ou data/hora ficarem vazios. Ao listar, mostre todas as reservas numeradas, indicando quais já foram confirmadas. Confirmar é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantas reservas existem no total, quantas já foram confirmadas e quantas ainda estão pendentes.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (na capacidade), aceitar uma reserva sem data e hora, tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido uma reserva válida.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de uma reserva?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido na capacidade?
- [ ] Testou confirmar uma reserva e ver isso refletido na listagem?
- [ ] Testou remover a única reserva da lista?

## Desafios extras (opcional)
- Permitir buscar uma reserva pelo recurso ou pelo responsável, em vez de só pelo número da lista.
- Ordenar a listagem pela data e hora.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
