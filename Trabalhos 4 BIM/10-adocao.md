# 10 Sistema de Adoção de Animais (Python)

## Contexto
Um abrigo de animais precisa de um jeito organizado de saber quais bichos estão disponíveis para adoção e quais já encontraram uma família. O grupo vai construir um sistema de linha de comando para esse controle, seguindo o mesmo padrão do sistema de controle de produtos usado como referência.

## O que cada animal guarda
Nome (obrigatório, até 100 caracteres), espécie (obrigatória, até 50 caracteres), idade (opcional, não pode ser negativa), porte (opcional, por exemplo "pequeno", "médio" ou "grande") e se já foi adotado (começa sempre como "não").

## Como guardar os dados
O grupo pode escolher entre duas formas de guardar os registros, e as duas são igualmente aceitas:

- **Vetores (listas paralelas)**: uma lista para cada campo (uma de nomes, uma de espécies, e assim por diante), todas com o mesmo tamanho e andando pelos mesmos índices. É o caminho mais parecido com o sistema de referência.
- **Matriz (lista de registros)**: uma lista só, onde cada posição guarda um animal completo com todos os seus campos juntos. É um pouco mais trabalhoso no começo, mas deixa cada registro mais fácil de mover, copiar ou remover inteiro.

Decidam qual das duas o grupo vai usar antes de escrever a primeira linha de código, e sigam com ela até o fim: trocar de estrutura no meio do caminho custa tempo.

## Roteiro sugerido
1. Cadastrar: sem isso não há o que listar depois.
2. Listar: assim você confirma visualmente que o cadastro está funcionando.
3. Remover: mais simples que atualizar, bom para pegar o jeito de mexer nos índices.
4. Atualizar: a etapa mais trabalhosa, deixe por último.
5. Relatório: só faz sentido depois de já existir dado cadastrado.

Teste cada etapa antes de passar para a próxima.

## Como deve se comportar
Ao cadastrar, pergunte cada campo e avise se nome ou espécie ficarem vazios. Ao listar, mostre todos os animais numerados, indicando quais já foram adotados. Marcar como adotado é uma ação separada, não uma edição comum. Atualizar deve permitir escolher qual campo mudar, um de cada vez. Remover deve pedir confirmação antes de apagar. O relatório mostra quantos animais existem no total, quantos já foram adotados e quantos ainda estão disponíveis.

## Erros que o sistema não pode deixar acontecer
Digitar letra onde era esperado número (na idade), tentar listar, atualizar ou remover com a lista vazia, ou confirmar remoção sem ter escolhido um animal válido.

## Antes de entregar, verifique
- [ ] Testou cadastrar mais de um animal?
- [ ] Testou listar com a lista vazia?
- [ ] Testou digitar um valor inválido na idade?
- [ ] Testou marcar um animal como adotado e ver isso refletido na listagem?
- [ ] Testou remover o único animal da lista?

## Desafios extras (opcional)
- Permitir buscar um animal pelo nome ou pela espécie, em vez de só pelo número da lista.
- Ordenar a listagem pela idade.
- Salvar os dados em um arquivo de texto, para não perder tudo ao fechar o programa.
