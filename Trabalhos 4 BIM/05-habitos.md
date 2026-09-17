# 05 Sistema de Rastreador de Hábitos (Python)

## Contexto
Criar um hábito novo é fácil, manter é que é difícil. O grupo vai construir um sistema de linha de comando para acompanhar quais hábitos estão sendo seguidos e por quantos dias seguidos, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada hábito guarda
Nome (obrigatório, até 100 caracteres), frequência (opcional, por exemplo "diária" ou "semanal"), sequência de dias seguidos cumprindo o hábito, o "streak" (opcional, não pode ser negativo, começa em zero), descrição (opcional, até 300 caracteres) e se já foi feito hoje (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de nomes, uma de frequências, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda um hábito completo com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se o nome ficar vazio. Ao listar, mostre todos os hábitos numerados, indicando quais já foram feitos hoje e o streak atual de cada um. Concluir hoje é uma ação separada: ela marca o hábito como feito hoje e soma um dia ao streak, não é uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantos hábitos existem no total, quantos já foram feitos hoje e quantos ainda faltam.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (no streak de dias), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido um hábito válido.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de um hábito?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido no streak de dias?
- [ ] Testou concluir um hábito hoje e ver o streak aumentar?
- [ ] Testou remover o único hábito da lista?

## Desafios extras (opcional)
- Permitir buscar um hábito pelo nome, em vez de só pelo número da lista.
- Ordenar a listagem pelo streak, do maior para o menor.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
