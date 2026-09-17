# 09 Sistema de Controle de Gastos Pessoais (Python)

## Contexto
No fim do mês fica difícil lembrar para onde foi o dinheiro. O grupo vai construir um sistema de linha de comando para registrar despesas pessoais e saber quais já foram pagas, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada despesa guarda
Descrição (obrigatória, até 150 caracteres), valor (obrigatório, maior que zero), categoria (opcional, até 50 caracteres), data (opcional, no formato AAAA-MM-DD) e se já foi paga (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de descrições, uma de valores, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda uma despesa completa com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se a descrição ficar vazia ou se o valor não for maior que zero. Ao listar, mostre todas as despesas numeradas, indicando quais já foram pagas. Marcar como paga é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantas despesas existem no total, quantas já foram pagas e quantas ainda estão em aberto.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (no valor), aceitar um valor zero ou negativo, tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido uma despesa válida.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de uma despesa?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor zero, negativo ou inválido para o valor da despesa?
- [ ] Testou marcar uma despesa como paga e ver isso refletido na listagem?
- [ ] Testou remover a única despesa da lista?

## Desafios extras (opcional)
- Permitir buscar uma despesa pela descrição ou categoria, em vez de só pelo número da lista.
- Ordenar a listagem pelo valor ou pela data.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
