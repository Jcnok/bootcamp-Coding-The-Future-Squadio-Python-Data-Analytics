# Resolução dos desafios de Código Python.

<img src="img/python.jpg" referrerpolicy="same-origin" style="display: block; object-fit: cover; border-radius: 0px; width: 100%; height: 30vh; opacity: 1; object-position: center 50%;">

<a name="ancora"></a>

# Desafios:

1. [A Aventura do Explorador](#ancora1)
2. [Lista de itens](#ancora2)
3. [Armazenamento de Dados é Vida](#ancora3)
4. [Organizando Os Seus Ativos](#ancora4)   
5. [O Grande Depósito](#ancora5)
6. [Validando a Força de Senhas no IAM](#ancora6)
7. [O Robô inteligente](#ancora7)   
8. [A Jornada da Classificação Frutífera](#ancora8)
9. [A Questão Intrincada da Magia Preditiva](#ancora9)  

<a name="ancora"></a>

<a id="ancora1"></a>
## Desafio: A Aventura do Explorador

### Descrição
Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!
 

### Entrada
* Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta.

### Saída
* O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.


### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:-----------------: 
1     | Explorador: 1 passo
2     | Explorador: 2 passos
----- | ------------------------------
----- | Explorador: 1 passo
3     | Explorador: 2 passos
----- | Explorador: 3 passos
----- | ------------------------------
----- | 
0     | Nenhum passo dado na floresta.
----- |

* **Código**:


```python
%%writefile codigos/execicio_iniciante_01.py
# Solicita ao usuário a entrada de um número inteiro positivo
quantidade_passos = int(input())

# Verifica se a quantidade de passos é zero
if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
else:
    # Utiliza um laço de repetição para simular os passos do explorador
    for passo in range(1, quantidade_passos + 1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")
```

    Writing codigos/execicio_iniciante_01.py


[voltar](#ancora)

<a id="ancora2"></a>
## Desafio: Lista de itens

### Descrição
Em um jogo de RPG, os personagens geralmente possuem uma lista de itens que podem ser utilizados durante o jogo. Esses itens podem ser armas, armaduras, poções de cura, entre outros. É importante que o jogador tenha um controle desses itens para poder utilizá-los no momento adequado.

Crie um programa que permita cadastrar uma lista de itens que o personagem possui. A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

### Entrada
O programa deve solicitar ao usuário o nome dos 3 itens que o personagem possui. Cada item deve ser cadastrado separadamente.

### Saída
Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela a lista de itens que o personagem possui. A saída deve ter o seguinte formato:

Lista de itens:
- [item1]
- [item2]
- [item3]

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
Espada       | Lista de itens:
Escudo       | - Espada
Poção        | - Escudo
-----        | - Poção
-----        | ---------------------------------
Gema         | Lista de itens:
Flecha       | - Gema
Capa         | - Flecha
-----        | - Capa
-----        | ---------------------------------
Masterball   | Lista de itens:
Potion       | - Masterball
Elixir       | - Potion
-----        | - Elixir

* **Código**:


```python
%%writefile codigos/execicio_iniciante_02.py
# Lista para armazenar os itens
itens = []

# Solicita os itens ao usuário
for i in range(3):
    item = input()
    itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")
```

    Writing codigos/execicio_iniciante_02.py


[voltar](#ancora)

<a id="ancora3"></a>
## Desafio:  Armazenamento de Dados é Vida

### Descrição
Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

### Entrada
- Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

### Saída
- A nova capacidade total em teraflops.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
100 20   | 120
-----    | ---------------------------------
50 10    | 55
-----    | ---------------------------------
200 50   | 300


* **Código**:


```python
%%writefile codigos/execicio_iniciante_03.py
# Entrada de dados
capacidade_atual, aumento_percentual = map(int, input().split())

# Calcula a nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Imprime a nova capacidade
print(int(nova_capacidade))
```

    Writing codigos/execicio_iniciante_03.py


[voltar](#ancora)

<a id="ancora4"></a>
## Desafio: Organizando Os Seus Ativos

### Desafio
Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

### Entrada:
A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

### Saída:
Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
3                         | Deposito
Financiamento de Imovel   | Financiamento de Imovel
Deposito                  | Reservas Bancarias
Reservas Bancarias        |
----- | ---------------------------------
3                         | Carteiras de credito 
Carteiras de credito      | Derivativos financeiros
Investimentos em titulos  | Investimentos em titulos
Derivativos financeiros   |
----- | ---------------------------------
3                         | Ativos intangiveis 
Reservas de liquidez      | Fundos de investimento
Ativos intangiveis        | Reservas de liquidez
Fundos de investimento    |

* **Código**:


```python
%%writefile codigos/execicio_intermediario_02.py
ativos = []
# Entrada da quantidade de ativos 
quantidadeAtivos = int(input())
# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for i in ativos:
  print(i)
```

    Writing codigos/execicio_intermediario_02.py


[voltar](#ancora)

<a id="ancora5"></a>
## Desafio: O Grande Depósito

### Desafio
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro e solicitar um novo valor. O programa deve continuar solicitando valores de depósito até que seja digitado um valor válido.

### Entrada
O programa deve utilizar o Scanner para receber os valores de depósito digitados pelo cliente. Os valores podem ser decimais, representando valores em reais.

### Saída
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro e solicitar um novo valor.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
500.50 | Deposito realizado com sucesso! Saldo atual: R$ 500.50
-----  | ---------------------------------
-100   | Valor invalido! Digite um valor maior que zero.
-----  | ---------------------------------
0      | Encerrando o programa...

* **Código**:


```python
%%writefile codigos/execicio_intermediario_01.py
saldo = 0 

while True:
 try:
  valor = float(input())

  if valor > 0:
   saldo = saldo + valor
   print("Deposito realizado com sucesso!")
   print("Saldo atual: R$ {:.2f}".format(saldo))
   break
  
  elif valor == 0:
   print("Encerrando o programa...")
   break

  else:
   print("Valor invalido! Digite um valor maior que zero.")

 except EOFError:
  break
```

    Overwriting codigos/execicio_intermediario_01.py


[voltar](#ancora)

<a id="ancora6"></a>
## Validando a Força de Senhas no IAM

### Desafio
Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

**Requisitos de segurança para a senha:**

1. A senha deve ter no mínimo 8 caracteres.
2. A senha deve conter pelo menos uma letra maiúscula (A-Z).
3. A senha deve conter pelo menos uma letra minúscula (a-z).
4. A senha deve conter pelo menos um número (0-9).
5. A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

### Entrada
A entrada será uma única string representando a senha que precisa ser validada.

### Saída
Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
0101             | Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.
-----            | ---------------------------------
030609saturno*   | Sua senha atende aos requisitos de seguranca. Parabens!
-----            | ---------------------------------
010203Jupiter    | Sua senha nao atende aos requisitos de seguranca.

* **Código**:


```python
%%writefile codigos/execicio_intermediario_03.py
import re

def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

    # Verificando se a senha contém letras maiúsculas, minúsculas, números e caracteres especiais
    for caractere in senha:
        if caractere.isupper():
            tem_letra_maiuscula = True
        elif caractere.islower():
            tem_letra_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif re.match(r'\W', caractere):
            tem_caractere_especial = True

    # Verificando se a senha atende a todos os critérios
    if not (tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial):
        return "Sua senha nao atende aos requisitos de seguranca."

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha e muito comum. Tente uma senha mais complexa."

    return "Sua senha atende aos requisitos de seguranca. Parabens!"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
```

    Writing codigos/execicio_intermediario_03.py


[voltar](#ancora)

<a id="ancora7"></a>
## Desafio: O Robô inteligente

### Desafio
Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

### Entrada
A entrada deve receber valores inteiros.

* numero: valor inteiro que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.

### Saída
O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
1      | positivo!
-1     | negativo!
2      | positivo!
0      | 2 números positivos, 1 números negativos
-----  | ---------------------------------
1      | positivo!
-1     | negativo!
0      | 1 números positivos, 1 números negativos
-----  | ---------------------------------
1      | positivo!
1      | positivo!
-1     | negativo!
-1     | negativo!
0      | 2 números positivos, 2 números negativos

* **Código**:


```python
%%writefile codigos/execicio_intermediarioII_01.py
# TODO: Crie a Função para classificar um número como positivo, negativo ou zero
def classificar_numero(numero):
    if numero > 0:
        return "positivo!"
    elif numero < 0:
        return "negativo!"
    else:
        return "zero!"

def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        # Chama a função classificar_numero para imprimir a classificação do número
        classificacao = classificar_numero(numero)
        print(classificacao)
        
        # TODO: Faça a verificação para saber quantos números positivos e negativos foram inseridos
        if classificacao == "positivo!":
            positivos += 1
        elif classificacao == "negativo!":
            negativos += 1
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()
```

    Writing codigos/execicio_intermediarioII_01.py


[voltar](#ancora)

<a id="ancora8"></a>
## Desafio: A Jornada da Classificação Frutífera

### Desafio
Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

* Morango:
  - Peso mínimo: 150 gramas
  - Textura: Suave (smooth)
  - Cor: Vermelha (red)
* Laranja:
  - Peso mínimo: 120 gramas
  - Textura: Suave (smooth)
  - Cor: Laranja (orange)
* Banana:
  - Peso mínimo: 150 gramas
  - Textura: Áspera (rough)
  - Cor: Amarela (yellow)
* Maçã:
  - Peso mínimo: 130 gramas
  - Textura: Ápera (rough)
  - Cor: Vermelha (red)
* Importante:
É necessário que a ordem das condições elif  seja respeitada conforme a descrição do desafio. Lembrando que, no Python, a indentação é fundamental para a definição de blocos de código, como os que pertencem a loops e funções. Se a indentação estiver incorreta, o Python não conseguirá interpretar corretamente o bloco de código, resultando em erros ou comportamento inesperado.

### Entrada
Seu código deve receber as seguintes entradas do usuário:

* Peso da fruta (em gramas): um número real que representa o peso da fruta.
* Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
* Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.

### Saída
O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.



Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
150        | ---
smooth     | A fruta é um morango!
red        | ---
-----      | ---------------------------------
140        | ---
rough      | Não foi possível classificar a fruta.
yellow     | ---
-----      | ---------------------------------
150        | ---
smooth     | A fruta é uma laranja!
orange     | ---


* **Código**:


```python
%%writefile codigos/execicio_intermediarioII_02.py
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    else:
        return "Não foi possível classificar a fruta."

# Entrada do usuário
try:
    peso_fruta = float(input())
    textura_fruta = input()
    cor_fruta = input()

    # Chamada da função de previsão
    resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

    # Saída da previsão
    print(resultado)
except ValueError:
    print("Por favor, insira valores válidos.")
```

    Writing codigos/execicio_intermediarioII_02.py


[voltar](#ancora)

<a id="ancora9"></a>
## Desafio: A Questão Intrincada da Magia Preditiva

### Desafio
No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.

Aqui estão os critérios mágicos para cada elemento:

* Elemento Fogo:

    * Intensidade do feitiço maior ou igual a 5.
    * Fase lunar durante o feitiço é crescente.
    * Idade do feiticeiro é superior a 100 anos.
* Elemento Água:

    * Intensidade do feitiço maior ou igual a 7.
    * Presença de componente raro.
    * Fase lunar durante o feitiço é cheia.
    * Idade do feiticeiro é igual ou inferior a 100 anos.
    * Afinidade com animais mágicos.
* Elemento Terra:

    * Intensidade do feitiço maior ou igual a 7.
    * Presença de componente raro.
    * Fase lunar durante o feitiço é cheia.
    * Idade do feiticeiro é igual ou inferior a 100 anos.
    * Afinidade com animais mágicos.
* Elemento Ar:

    * Caso não se encaixe nos critérios anteriores.

### Entrada
Seu código deve receber as seguintes entradas do usuário:

* Intensidade do feitiço (de 1 a 10): um número inteiro representando a força do feitiço.
* Componente raro (sim ou não): uma string indicando se o feitiço contém um componente raro.
* Fase lunar (cheia, crescente ou minguante): uma string indicando a fase lunar durante o lançamento do feitiço.
* Idade do feiticeiro (em anos): um número inteiro representando a idade do feiticeiro.
* Afinidade com animais mágicos (sim ou não): uma string indicando se o feiticeiro tem afinidade com animais mágicos.

### Saída
O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos atributos fornecidos.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
6            | ---
sim          | A afinidade elemental do feiticeiro é com o elemento Fogo!
crescente    | ---
110          | ---
sim          | ---
-----        | ---------------------------------
8            | ---
sim          | A afinidade elemental do feiticeiro é com o elemento Água!
cheia        | ---
80           | ---
não          | ---
-----        | ---------------------------------
9            | ---
sim          | A afinidade elemental do feiticeiro é com o elemento Terra!
cheia        | ---
80           | ---
sim          | ---


* **Código**:


```python
%%writefile codigos/execicio_intermediarioII_03.py
# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"
    
    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    elif intensidade >= 7 and componente_raro and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais:
        return "A afinidade elemental do feiticeiro é com o elemento Terra!"
    elif intensidade >= 7 and componente_raro and fase_lunar == "cheia" and idade_feiticeiro <= 100:
        return "A afinidade elemental do feiticeiro é com o elemento Água!"
    else:
        return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input())
afinidade_animais_feiticeiro = input()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)
```

    Writing codigos/execicio_intermediarioII_03.py


[voltar](#ancora)
