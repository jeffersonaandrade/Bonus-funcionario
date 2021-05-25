import pandas as pd
from twilio.rest import Client

#Imports baixados: Pandas, Openpyxl, Twilio.

# Adicionar o seu ID cadastrado na plataforma
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Adicionar o seu token cadastrado na plataforma
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)


# ABRIR AS PLANILHAS DE EXCEL

# PARA CADA ARQUIVO

lista_nome = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_nome:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Realizei um processo de formataçao colocano o f na frente, e puxando a o nomes dos meses listados anteriormente
# VERIFICAR SE ALGUM VALOR NA COLUNA VENDAS É > 55.OOO
    if (tabela_vendas ['Vendas'] > 55000).any():
        vendedor= tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas= tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, 'Vendas'].values[0]
        #AQUI PESQUISO A LINHA BASEADA NUMA CONDICAO. QUE É A LINHA QUE TENHA UM NUMERO MAIOR QUE 55000.
        #LOC É O MODO PESQUISA DO PYTHON NESSA TAREFA, OU SEJA, LOC DE LOCALIZAR.
        #tabela_vendas ['Vendas'] > 55000 onde estaria isso, seria o termo linha
        #e onde estaria o vendedor ou vendas, o termo genérico seria coluna.
        #Porém o loc sempre te volta uma tabela, mesmo que tenha apenas um numero delo dela, por isso, usamos o values.
        #em grosso modo, estamos jogando fora a tabela, e ficando apenas com o valor.
        #print(f'No mes de {mes}  alguém bateu a meta! vendedor: {vendedor} vendas: {vendas}')
# SE FOR > 55 MIL ENVIAR SMS
# SMS COM NOME, MES E AS VENDAS DO VENDEDOR
        message = client.messages.create(
            to="+15558675309",  # numero pra quem ele enviará o sms
            from_="+15017250604",  # número cedido pela plataforma do twilio
            body=f'No mes de {mes}  alguém bateu a meta! vendedor: {vendedor} vendas: {vendas}')

        print(message.sid)




