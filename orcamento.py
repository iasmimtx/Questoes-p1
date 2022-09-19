uniTijolo = float(input('Digite o preço da unidade do tijolo (Em reais): '))
altTijolo = float(input('Digite a altura do tijolo (Em metros): '))
compTijolo = float(input('Digite o comprimento do tijolo (Em metros): '))
altparedes = float(input('Digite a altura das paredes (Em metros): '))
compParedes = float(input('Digite o comprimento das paredes (Em metros): '))

num_tijolo_altura = altparedes / altTijolo
num_tijolo_largura = compParedes / compTijolo
total_tijolos = num_tijolo_altura * num_tijolo_largura
orcamento_total = total_tijolos * uniTijolo

print(f'O número total de tijolos é {total_tijolos:.1f} e o orçamento final é de R$ {orcamento_total:.1f}')
