import random

class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = round(random.uniform(10, 500), 2)

    def mostra_saldo(self):
        print(f"Benvenuto {self.nome}! Il tuo saldo è: €{self.saldo}")



# Classe base (madre)
class MetodoPagamento:
    def effettua_pagamento(self, importo, saldo): # metodo che i figli sovrascriveranno
        pass  # le classi figlie sovrascriveranno questo metodo


# Classe figlia - applica una commissione del 2%
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo, saldo):
        commissione = importo * 0.02
        totale = importo + commissione
        print(f"Carta di Credito: €{importo} + €{commissione} commissione = €{totale}")
        return saldo - totale


# Classe figlia - applica una commissione del 3%
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo, saldo):
        commissione = importo * 0.03
        totale = importo + commissione
        print(f"PayPal: €{importo} + €{commissione} commissione = €{totale}")
        return saldo - totale


# Classe figlia - applica una commissione fissa di €1.50
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo, saldo):
        commissione = 1.50
        totale = importo + commissione
        print(f"Bonifico: €{importo} + €{commissione} fissi = €{totale}")
        return saldo - totale


# GestorePagamenti riceve un'istanza di MetodoPagamento (o una sua figlia)
# e la usa senza sapere quale metodo di pagamento è
class GestorePagamenti:
    def __init__(self, metodo):
        self.metodo = metodo  # salva l'istanza ricevuta, contiene un MetodoPagamento. crea questa variabile che dopo in base a come è chiamata chiama una classe

    def paga(self, importo, saldo):
        # polimorfismo: chiama effettua_pagamento() senza sapere se è CartaDiCredito, PayPal o Bonifico
        return self.metodo.effettua_pagamento(importo, saldo) #per ora saldo è una variabile ancora da riempire, dopo lo identifico con quello dell'utente


#programma
utente = Utente("Niki")
utente.mostra_saldo()


importo = float(input("Quanto vuoi pagare? €"))

print("\nScegli il metodo di pagamento:")
print("1 - Carta di Credito (commissione 2%)")
print("2 - PayPal (commissione 3.5%)")
print("3 - Bonifico Bancario (commissione fissa €1.50)")

scelta = input("\nInserisci il numero: ")

# in base alla scelta creiamo l'istanza giusta (tutte figlie di MetodoPagamento)
if scelta == "1":
    metodo = CartaDiCredito()
elif scelta == "2":
    metodo = PayPal()
elif scelta == "3":
    metodo = BonificoBancario()
else:
    print("Scelta non valida!")
    exit()

# passiamo l'istanza al gestore  lui non sa quale è, chiama paga() e basta
gestore = GestorePagamenti(metodo)
nuovo_saldo= gestore.paga(importo,utente.saldo) 




if nuovo_saldo >= 0:
    utente.saldo = nuovo_saldo
    print(f"Pagamento effettuato! Ti restano €{utente.saldo}")
else:
    print(f"Saldo insufficiente!")


