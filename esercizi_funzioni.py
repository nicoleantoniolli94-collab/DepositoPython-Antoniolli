'''1. Esercizio Base: Indovina il numero 
Descrizione: Scrivi un programma che genera un numero casuale
tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
stato generato. Dopo ogni tentativo, il programma dovrebbe
dire all'utente se il numero da indovinare è più alto o più
basso rispetto al numero inserito. Il gioco termina quando
l'utente indovina il numero o decide di uscire.'''


import random
 
 
def genera_numero():
    # Genera e restituisce un numero casuale tra 1 e 100
    return random.randint(1, 100)
 
 
def indovina(numero_segreto):
    # Continua a chiedere il numero finché l'utente non indovina o esce
    while True:
        numero_scelto = input("Inserisci un numero x per uscire: ")
        # Se l'utente inserisce 'x' abbandona il gioco
        if numero_scelto.lower() == 'x':
            print(f"Hai abbandonato. Il numero era: {numero_segreto}")
            break
        numero_scelto = int(numero_scelto)
        # Confronta il tentativo con il numero segreto
        if numero_scelto < numero_segreto:
            print("Troppo basso!")
        elif numero_scelto > numero_segreto:
            print("Troppo alto!")
        else:
            print("Hai indovinato!")
            break
 
 
# Genera il numero segreto e avvia il gioco
numero_segreto = genera_numero()
indovina(numero_segreto)


