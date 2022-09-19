veiculo = str(input())

if veiculo == "Ônibus" or veiculo == "Caminhão":
   quant_eixo = int(input())

   if veiculo == "Caminhão":
       caminhao = quant_eixo * 9.60
       print(f"Valor a pagar: R$ {caminhao:.2f}.")
   elif veiculo == "Ônibus":
       onibus = quant_eixo * 11.40
       print(f"Valor a pagar: R$ {onibus:.2f}.")

elif veiculo == "Automóvel utilitário":
        print(f"Valor a pagar: R$ 11.40.")

elif veiculo == "Motocicleta":
    print(f"Valor a pagar: R$ 5.70.")

else:
    print("Veículo não cadastrado.")