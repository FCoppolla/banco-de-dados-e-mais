import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="backend-aula1.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query1 = "SELECT nome, idade, naturalidade from aluno where sexo = 'M' and naturalidade = 'Rio de Janeiro' "
cursor. execute (query1)
resultados1 = cursor.fetchall()

for linha in resultados1:
    print(linha)


query2 = "select nome, sexo, naturalidade from aluno where sexo ='F' and naturalidade = 'São Paulo' "

cursor.execute(query2)
# Processar os resultados
resultados2 = cursor.fetchall()

# Classificação dos alunos
for linha in resultados2:  
    print(linha)

    
        
    
    
# Fechando o cursor e a conexão
cursor.close()
cnx.close()

