import os
import wget
from datetime import datetime, date
import time
import pandas as pd

# Cria diretória onde arquivo será salvo
# def cria_diretorio():
#     if os.system('ls -ll /arquivos_hd/Pessoal/projetos/cgu/') != 'total 0':
#         os.system('rm -rf /arquivos_hd/Pessoal/projetos/cgu/arquivo/* && mkdir -p /arquivos_hd/Pessoal/projetos/cgu/arquivo/')
#     else:
#         os.system('mkdir -p /arquivos_hd/Pessoal/projetos/cgu/arquivo/')
# cria_diretorio()

#Recupera data atual
dt = date.today()
data_atual = int(dt.strftime("%Y%m%d")) - 1
print('Esse é o arquivo do dia: ' + str(data_atual))

url = ('https://www.portaltransparencia.gov.br/download-de-dados/despesas/' + str(data_atual))

#Verifica se url esta disponivel
curl = os.popen('curl --write-out %{http_code} --silent --output /dev/null https://www.portaltransparencia.gov.br/download-de-dados/despesas/' + str(data_atual)).read()
#print(type(curl))

count = 1

while count <= 5:
    print('Testando o endereço do arquivo')
    if curl == '200':
        print('O endereço url está disponível \nRealizando o download do arquivo')
        file = wget.download(url)
        #os.system('scp /')
        break
    else:
        print('Deu Errado! Essa é a ' + str(count) + 'ª' + ' tentativa:' )
        time.sleep(15)
    print('Download não realizado')
    count += 1

# Move arquivo para outro diretório
os.system('mv /arquivos_hd/Pessoal/projetos/cgu/' + file + ' /arquivos_hd/Pessoal/projetos/cgu/arquivo/')
time.sleep(5)

# Descompacta arquivo
os.system('unzip /arquivos_hd/Pessoal/projetos/cgu/arquivo/' + file + ' -d /arquivos_hd/Pessoal/projetos/cgu/arquivo/')

dataframe = pd.read_csv('/arquivos_hd/Pessoal/projetos/cgu/arquivo/' + str(data_atual) + '_Despesas_Pagamento.csv', sep=';')
<<<<<<< HEAD

=======
>>>>>>> 8d8771a (comitando alterações no código)
dataframe

# if curl == '200':
#     print('Deu certo')

#wget arquivo csv CGU
# site = ('https://www.portaltransparencia.gov.br/download-de-dados/despesas/{}'.format(data_atual))
# file = wget.download(site)

#Realizando download do arquivo csv
#os.system('wget -O /backup/backup/sinc_dump/cgu/ext/%s/%s_gastodireto.zip "https://www.portaltransparencia.gov.br/download-de-dados/despesas/data_atual"' % (df_list[0][1], df_list[0][1], df_list[0][1]))
#https://www.portaltransparencia.gov.br/download-de-dados/despesas/20220801
