



# MENU ESERCIZI

# il menu si ripresenta dopo ogni esercizio
while True:

    # Stampiamo le opzioni disponibili
    print("\n MENU ESERCIZI")
    print("1 - Pari o Dispari")
    print("2 - Countdown")
    print("3 - Quadrati")
    print("4 - Analisi lista ")
    print("0 - Esci")

    scelta = input("\nScegli il numero dell esercizio: ")

    match scelta:
        
        # ESERCIZIO 1 
        #Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
        #e "Dispari" se il numero è dispari
      
        case "1":
            numero = int(input("Inserisci un numero: "))

            # if controlla se il resto della divisione per 2 è 0 allora pari
            if numero % 2 == 0:
                print("Pari")
            # altrimenti dispari
            else:
                print("Dispari")

        
        # ESERCIZIO 2
        #Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
        #numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripete all’infinito
        
        case "2":
           while True:  # Il sistema si ripete all'infinito finché l'utente non decide di uscire
                n = int(input("Inserisci un numero intero positivo: (0 per uscire):"))
                
                # Se l'utente inserisce 0 usciamo dal ciclo e terminiamo il programma
                if n == 0:
                     print("Uscita dal programma!")
                     break

                # Controlliamo che il numero sia positivo
                elif n <= 0:
                   print("Errore: inserisci un numero intero positivo!")
                else:
                  # range(n, -1, -1) parte da n e arriva a 0 compreso, decrementando di 1
                  for i in range(n, -1, -1):
                     print(i)

                     print("fine :)")

        
        # ESERCIZIO 3 
        # Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
        # ciascun numero nella lista.
      
        case "3":
            
            numeri = []  # Lista vuota

            print("Inserisci i numeri uno alla volta (scrivi "fine" per terminare):")

            # Raccogliamo i numeri dall'utente finché non preme invio vuoto
            while True:
                valore = input("Numero: ")

                # Se l'utente scrive "fine" usciamo dal ciclo
                if valore == "fine":
                    break

                # Altrimenti aggiungiamo il numero alla lista
                numeri.append(int(valore))

            # Ciclo for: itera ogni numero e ne stampa il quadrato
            for num in numeri:
                print(f'il quadrato di {num} è {num ** 2}')


       
        # ESERCIZIO 
        
        case "4":
            lista = []  # Lista vuota

            print("Inserisci i numeri uno alla volta (scrivi "fine" per terminare):")

            # Raccogliamo i numeri dall'utente finché non preme invio vuoto
            while True:
                valore = input("Numero: ")

                # Se l'utente scrive "fine" usciamo dal ciclo
                if valore == "fine":
                    break

                # Altrimenti aggiungiamo il numero alla lista
                lista.append(int(valore))

          #Utilizzare un ciclo for per trovare il numero massimo nella lista.
            massimo = lista[0]  # Inizializziamo il massimo al primo elemento della lista

            for num in lista:
                if num > massimo:
                    massimo = num

            print(f'Il numero massimo nella lista è: {massimo}')
            
        #Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
            count = 0
            index = 0

            while index < len(lista):
                count += 1
                index += 1

            print(f'Il numero di elementi nella lista è: {count}')
            
    # Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
    # altrimenti stampare il numero massimo trovato e il numero di elementi nella lista
            if len(lista) == 0:
                print("Lista Vuota")
            else:
                print(f'Il numero massimo nella lista è: {massimo}')
                print(f'Il numero di elementi nella lista è: {count}')

        
        # USCITA
        
        case "0":
            print("Arrivederci!")
            break  # Usciamo dal loop

        # Caso default: scelta non riconosciuta
        case _:
            print("Scelta non valida. Riprova.")
            
            