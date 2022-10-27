valor_sem_desconto = float(input("Valor original: R$ "))
desconto = float(input("Desconto (em %) para esse produto: "))
desconto = desconto / 100
print('Valor original:     R$', valor_sem_desconto)
print('Desconto ganho:     R$', valor_sem_desconto * desconto)
print('Valor com desconto: R$', valor_sem_desconto * (1 - desconto))
