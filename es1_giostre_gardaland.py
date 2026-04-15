# 1. crea delle condizioni 

# chiedi età , altezza, peso per salire su una giostra

print('Benvenuto a Gardaland!')
eta = int(input('inserisci la tua età:'))
altezza = float(input('inserisci la tua altezza:'))
peso = float(input('inserisci il tuo peso:'))

if eta >= 10:
    if altezza >= 150:
        if peso >= 50:
            print('puoi salire sul BlueTornado!')
else:
    print('Ci dispiace, non puoi salire sul BlueTornado')