# 08 Sistema de Cuidado com Plantas (Python)

## Contexto
Regar as plantas no dia certo é fácil de esquecer, e é assim que elas acabam murchando. O grupo vai construir um sistema de linha de comando para acompanhar quando cada planta precisa de água e se está saudável, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada planta guarda
Nome (obrigatório, até 100 caracteres), espécie (opcional, até 100 caracteres), frequência de rega em dias (obrigatório, não pode ser negativo), data da última rega (opcional, no formato AAAA-MM-DD) e se está saudável (começa sempre como "sim"; o padrão aqui é o oposto dos outros temas, já que uma planta recém-cadastrada é considerada saudável até que se prove o contrário).

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de nomes, uma de espécies, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda uma planta completa com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se nome ou frequência de rega ficarem vazios. Ao listar, mostre todas as plantas numeradas, indicando quais estão saudáveis. Regar é uma ação separada: ela apenas atualiza a data da última rega para a data atual, não é uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez, incluindo marcar uma planta como não saudável, caso o grupo perceba esse cenário. Remover deve pedir confirmação antes de apagar. O relatório mostra quantas plantas existem no total, quantas estão saudáveis e quantas não estão.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (na frequência de rega), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido uma planta válida.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de uma planta?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido na frequência de rega?
- [ ] Testou regar uma planta e ver a data atualizada na listagem?
- [ ] Testou remover a única planta da lista?

## Desafios extras (opcional)
- Permitir buscar uma planta pelo nome, em vez de só pelo número da lista.
- Ordenar a listagem pela frequência de rega.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
