# importando biblioteca
import calendar 
from datetime import date


#exibindo a data atual
dia = date.today().day
mes = date.today().month
ano = date.today().year

# tupla
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#saida de dados
print(f'Data atual: {dia} de {meses[mes - 1]} de {ano}.\n')
print('Mês atual')
print(calendar.month(ano, mes))