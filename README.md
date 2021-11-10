# 10ª Maratona de Programação Interfatecs
Repositório dos códigos desenvolvidos para a 10ª edição da Maratona de Programação Interfatecs.

Todos os problemas foram resolvidos em Python, sendo feita após a maratora uma otimização dos mesmos em C/C++.

Códigos desenvolvidos por Anthony Almeida Andrade e Giulia Ventura Ratti.

# Problemas Resolvidos
 - **Fluxonator ([B](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/B.pdf))**\
 É feita a leitura das entradas e armazenamento das direções para cada ponto de entrada (-1 para esquerda e 1 para direita - pontos A, B e C).\
 Para cada entrada lida, é feita a verificação das direções e imprimida na tela a saída.

 - **Azeitonas na Pizza ([C](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/C.pdf))**\
É feita a leitura e verificação de dois números inteiros 'X' e 'Y', imprimindo as posições para os pontos, alternando entre positivos, negativos e suas posições.

 - **Estacionamento do Seu Zé ([E](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/E.pdf))**\
É feita a leitura de placas enquanto não EOF, sendo cada uma transformada em um código "ASCII" para verificação de qual posição do estacionamento aquela placa irá ocupar.\
Por fim, é imprimido na tela as posições ocupadas e as placas que as ocupam.

 - **SquareCity ([F](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/F.pdf))**\
É lido somente um número inteiro 'X' e feito o cálculo de uma 'base' e um 'mult':\
\- mult: De 1 até X, pulando 4, é somado 2\
\- base: Valor referente ao 'mult + 1'\
Foi feita a verificação pelo X, se nas bordas da cidade estão contidas ruas ou casas e feita o cálculo e impressão na tela com base nos valores.

 - **Programando o Resgate ([K](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/K.pdf))**\
 É lido os dados e feita uma análise dos quartos e suas conexões, anulando os que contém terroristas.\
 Na análise dos quartos, calculamos todas as conexões possíveis partindo do ponto inicial dos reféns e, independente de ordem, verificamos se é possível chegar na saída.
 
# Resolvidos, porém *Incorretos*
Para ambos os problemas a seguir, foi feita a leitura e cálculo dos dados, com a apresentação correta dos valores. Por mais que nossas saídas estavam corretas para todas as entradas, não conseguimos identificar o que estava incorreto para a correção a tempo do problema.

- **As Fotos da Ana Maria ([D](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/D.pdf))**\
Após a leitura dos valores, é feito para cada número a divisão com a soma de todos, apresentando o resultado na tela com 3 casas decimais, removendo zeros caso necessário. 

- **De quem é esse Jegue? ([G](https://github.com/chocothony/decima-maratona-programacao-interfatecs/blob/main/PDFs/G.pdf))**\
É feito a leitura dos valores até EOF, sendo guardado os nomes e tempos, sendo criado arrays para 'backup' dos dados.\
Após isso, é feita a ordenação dos tempos e obtenção dos indexes dos 3 menores valores para cada um dos arrays de tempo, apresentando os nomes correspondente ao tempos. 
