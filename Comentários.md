
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Juan Gustavo  
**Turma:** Rio Negrinho — Tarde  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Delivery de comida  
**Código analisado:** `codigo/app.py`  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Juan, você iniciou um sistema de delivery com opções de hambúrgueres, bebidas e sobremesas. O programa apresenta uma ideia definida e demonstra seus primeiros passos na utilização de entrada de dados e estruturas condicionais.

Pontos positivos identificados:

- Escolheu um tema previsto na Situação de Aprendizagem.
- Criou um cardápio dividido em categorias de produtos.
- Utilizou **`input()` e `int()`** para receber opções do usuário.
- Aplicou **`if` e `elif`** para associar escolhas a produtos.
- Começou a utilizar variáveis como `nome` e `preco` para representar os itens selecionados.
- Definiu produtos e preços que poderão ser aproveitados na continuidade do projeto.

## O que precisa ser corrigido

### 1. Reorganizar os blocos condicionais

A indentação dos blocos `if` e `elif` não está consistente. A leitura da categoria e a escolha de produtos aparecem em níveis que misturam as decisões do cardápio.

Por exemplo, a pergunta "escolha seu lanche" aparece fora do bloco específico de hambúrgueres, embora o usuário também possa escolher bebidas ou sobremesas.

**Como melhorar:** criar uma condição principal para cada categoria e, dentro dela, colocar as opções correspondentes. Mantenha a indentação com quatro espaços por nível.

### 2. Tratar opções inválidas

O programa não garante que as variáveis `nome` e `preco` sejam preenchidas quando uma escolha não corresponde a nenhum produto.

**Como melhorar:** definir uma resposta para cada opção inválida e impedir que o fluxo continue sem um produto selecionado. Também é necessário tratar letras e campos vazios antes de converter o valor com `int()`.

### 3. Corrigir inconsistências do cardápio

O X-Burger aparece no cardápio por R$ 25,00, mas o código atribui R$ 27,00 à variável `preco` quando esse produto é selecionado.

**Como melhorar:** conferir todos os produtos e preços, garantindo que o valor apresentado ao cliente seja igual ao utilizado no cálculo.

### 4. Concluir a funcionalidade inicial

O código termina após as condições de seleção de produtos. Ainda não existe um resumo que confirme claramente o item escolhido, a quantidade ou o valor do pedido.

**Como melhorar:** concluir inicialmente um fluxo simples:

1. Mostrar as categorias.
2. Permitir selecionar uma categoria e um produto.
3. Verificar a validade da escolha.
4. Informar o produto selecionado e seu preço.
5. Encerrar ou permitir uma nova operação.

Não é necessário construir todas as funcionalidades de um delivery de uma só vez.

## Oportunidades de melhoria

### 5. Organizar o cardápio em dicionários

Atualmente, os produtos e preços estão distribuídos em várias condições.

**Como melhorar:** criar um dicionário para armazenar os produtos e seus respectivos preços. Isso facilitará a consulta e evitará diferenças entre os valores anunciados e os valores utilizados.

### 6. Criar funções

O programa ainda não possui funções definidas pelo estudante.

**Como melhorar:** começar por funções simples, como `mostrar_cardapio()`, `selecionar_produto()` e `mostrar_resumo()`. Uma função deve executar uma tarefa identificável e retornar um resultado quando necessário.

### 7. Documentar e testar o programa

Não há comentários explicativos suficientes sobre o funcionamento e as regras do sistema.

**Como melhorar:** adicionar explicações curtas aos blocos principais e atualizar o README com o objetivo do projeto, as funcionalidades existentes e a forma de execução.

## Testes recomendados

1. Escolher um hambúrguer válido.
2. Escolher uma bebida válida.
3. Escolher uma sobremesa válida.
4. Digitar uma categoria inexistente.
5. Digitar letras em vez de números.
6. Selecionar um produto inexistente.
7. Conferir se o produto e o preço apresentados estão corretos.

## Prioridades para a próxima versão

1. **Corrigir a indentação e a organização das condições.**
2. **Concluir um fluxo funcional de seleção e resumo do pedido.**
3. **Tratar entradas inválidas.**
4. **Corrigir os preços divergentes.**
5. **Criar funções e documentar os testes realizados.**

## Mensagem final

Juan, você já iniciou seu projeto e demonstrou que compreende a ideia de utilizar **entradas e condições** para construir um cardápio interativo. Esse é um primeiro passo importante.

Agora, concentre-se em terminar uma funcionalidade pequena e fazê-la funcionar corretamente antes de adicionar novos recursos. **Organizar os blocos, testar cada escolha e corrigir os resultados será essencial para sua evolução.** Continue praticando: a clareza do código e a capacidade de resolver erros são habilidades construídas com exercício e persistência.
