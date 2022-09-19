# coding: utf-8
# Calculando o consumo de energia em kwh

potencia = int(input())
duracao = int(input())
tempo = duracao / 60         
kwh = (potencia * tempo) / 1000
print (f'{kwh:.1f} kWh')  
                  

