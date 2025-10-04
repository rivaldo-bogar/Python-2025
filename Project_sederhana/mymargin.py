# Calculasi otomatis uang saya
mycash = float(input("\nNominal margin : Rp."))
inp_laverage = float(input("\nRencana laverage : X"))

margin_pluslvg = mycash * inp_laverage
print(f'\nMONEY INFORMATION\nPosisi margin nyata anda = Rp.{mycash:.3f}')
print(f'Posisi laverage anda = Rp.{int(margin_pluslvg)}\n')

margincall_price = (margin_pluslvg / 100)*1
print(f'{margincall_price}')
start = 2
mycash = int(mycash)
print(f"{mycash}")
print(f"{margincall_price}")
for margincall_price in range(mycash):
    if margincall_price <= mycash:
        margincall_price *= start
        start +=1
    else:
        print(f"Margincall terpenuhi, Anda terlikuidasi")
margincall_price = float(margincall_price)
print(f"Margin terpenuhi sekitar {margincall_price} percentase {int(start)}%")