#!/usr/bin/python

import psycopg
import psycopg2
import numpy as np
from datetime import datetime
from datetime import date
import pandas as pd
import os

#Os registros de conexão não são reais
def conecta_db():
    con = psycopg2.connect(
        host='localhost',
        database='nm_db',
        port='5432',
        user='nm_user',
        password='senha_user'
    )
    return con

def consulta_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros

#Consulta base de dados fake para coleta de hora atual
reg = list(consulta_db("select data_atual from data WHERE data = 'data_hoje'"))

# Tranformando os dados da consulta no PostegreSQL em DataFrame
df_bd = pd.DataFrame(reg, columns=['data_hora'])

#Cria coluna 'data' a partir da coluna data_hora, retirando o registro de hora
df_bd['data'] = df_bd['data_hora'].dt.strftime('%Y%m%d')
df_bd['ano_mes'] = df_bd['data_hora'].dt.strftime('%Y%m')

#Converte DataFrame em Lista
df_list = df_bd.values.tolist()

def cria_diretorio():
    if os.system('ls -ll /diretorio/meu_diretorio/') != 'total 0':
        os.system('rm -rf /diretorio/meu_diretorio/* && mkdir -p /diretorio/meu_diretorio/%s' % (df_list[0][1]))
    else:
        os.system('mkdir -p /diretorio/meu_diretorio/%s' % (df_list[0][1]))
cria_diretorio()

#Download arquivos despesas
os.system('wget -O /diretorio/meu_diretorio/%s/%s_gastodireto.zip "https://www.portaltransparencia.gov.br/download-de-dados/despesas/%s"' % (df_list[0][1], df_list[0][1], df_list[0][1]))

#Download arquivos favorecidos
os.system('wget -O //diretorio/meu_diretorio/%s/%s_favorecidos.zip "https://www.portaltransparencia.gov.br/download-de-dados/favorecidos-pj/202102"' % (df_list[0][1], df_list[0][2]))

#Descompacta Gasto direto
os.system('unzip -o //diretorio/meu_diretorio/%s/%s_gastodireto.zip -d //diretorio/meu_diretorio/%s/' % (df_list[0][1], df_list[0][1], df_list[0][1]))

#Descompacta Favorecidos
os.system('unzip -o //diretorio/meu_diretorio/%s/%s_favorecidos.zip -d //diretorio/meu_diretorio/%s/' % (df_list[0][1], df_list[0][2], df_list[0][1]))

#SCP arquivos .csv para servidor que irá consumir

os.system('scp //diretorio/meu_diretorio/%s/%s_Despesas_Pagamento.csv root@ip://diretorio/meu_diretorio/' % (df_list[0][1], df_list[0][1]))
os.system('scp //diretorio/meu_diretorio/%s/202102_CNPJ.csv root@192.168.24.11://diretorio/meu_diretorio/' % (df_list[0][1]))
os.system('scp //diretorio/meu_diretorio/%s/202102_CNAE.csv root@192.168.24.11://diretorio/meu_diretorio/' % (df_list[0][1]))
os.system('scp //diretorio/meu_diretorio/%s/202102_NaturezaJuridica.csv root@ip://diretorio/meu_diretorio/' % (df_list[0][1]))