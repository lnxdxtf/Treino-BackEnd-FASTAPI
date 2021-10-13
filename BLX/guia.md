#####   START SERVE ==>  
        uvicorn src.server:app --reload --reload-dir=src

#####   ativar ambiente virtual     
           .\env1\Scripts\Activate.ps1
-------------------------------------------------------------------------

### ALEMBIC

>O ALEMBIC  ajuda o banco de dados a evoluir. Adicionando tabelas/colunas/etc.

    Alembic revision --autogenerate -m "NOME DA REVISÃO/VERSÃO"
Vai criar uma versão do banco de dados(bd). Liberando o upgrade e downgrade do bd.

##### Upgrade
    alembic upgrade head
Vai atualizar para a versão/revisão mais recente

#### Exemplo:
Atualizar a classe Produto que dá o modelo do bd. no arquivo (models.Produto) , adicionando a variavel de tamanho. 

##### Passos:

1- adicione a variavel tamanho como coluna de string (tamanho=Column(String))

2- executar o comando alembic de revisão/versão para detectar essa alteração do modelo do bd.

3- em (alembic/versions/) vai ser gerado o arquivo .py mostrando as funções do comando para atualizar.
Se o alembic detectou a alteração ele vai preencher a função.
Se ele não detectou ele vai fazer essas funçõe vazias (pass)

4- para efetivar a atualização do banco de dados utilize o coamndo de upgrade (-| alembic upgrade head |-)

5 - atualize o bd e verifique se está tudo certo

##### Downgrade
        alembic downgrade base
Vai voltar para a primeira versão. Podemos substituir o "base" pelo nome da versão.

