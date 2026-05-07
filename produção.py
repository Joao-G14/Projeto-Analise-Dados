import pandas as pd
import numpy as np

df = pd.read_csv('Produção.xlsx - BaseProdução.csv')

df['Data Inicio'] = pd.to_datetime(df['Data Inicio'])

df['Ocorrência'] = df['Ocorrência'].fillna('')

total_aprovado = df['Qtd Aprovada'].sum()
total_rejeitado = df['Qtd Rejeitada'].sum()
total_produzido = total_aprovado + total_rejeitado

df['Status_Producao'] = np.where(df['Ocorrência'] == '', 'Produtiva', 'Parada')

horas_produtivas = df[df['Status_Producao'] == 'Produtiva']['Total Horas'].sum()
horas_paradas = df[df['Status_Producao'] == 'Parada']['Total Horas'].sum()
tempo_total_disponivel = horas_produtivas + horas_paradas

disponibilidade = (horas_produtivas / tempo_total_disponivel) if tempo_total_disponivel > 0 else 0

qualidade = (total_aprovado / total_produzido) if total_produzido > 0 else 0

df['Mes_Ano'] = df['Data Inicio'].dt.to_period('M')
aprovado_por_mes = df.groupby('Mes_Ano')['Qtd Aprovada'].sum().reset_index()


print(f"--- RESUMO DE PRODUÇÃO ---")
print(f"Total Aprovado: {total_aprovado}")
print(f"Total Rejeitado: {total_rejeitado}")
print(f"Horas Produtivas: {horas_produtivas:.2f}h")
print(f"Horas Paradas: {horas_paradas:.2f}h")
print(f"Disponibilidade: {disponibilidade:.2%}")
print(f"Qualidade: {qualidade:.2%}")
print("\n--- TOTAL APROVADO POR MÊS ---")
print(aprovado_por_mes)

