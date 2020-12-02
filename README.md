
#Inverted Index  
Este projeto tem o objetivo de gerar um índice invertido de palavras
contidas em vários arquivos, de forma que seja possível a busca rápida
por todos os arquivos que contem a palavra desejada.

O projeto foi desenvolvido em python com o uso da biblioteca PySpark.


#Modo de Execução  
O projeto usa pipenv para gerenciamento de dependências e criação de ambientes
virtuais, logo é necessário tê-lo instalado.

Caso não o tenha execute o comando no terminal:
**pip install pipenv**

Feito isso execute o comando
**pipenv install**
para criar o ambiente virtual e instalar as dependências.

Por fim basta executar **python main.py** na raiz do projeto.

Serão criados dois arquivos, _dictionary_ e _inverted_index_.
O primeiro contem o dicionario de palavras e seus Ids, o segundo contem o
índice invertido onde cada Id de palavra vem seguido dos Ids dos documentos
que contém aquela palavra.
