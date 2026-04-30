
# File che raccoglie tutte le prenotazioni effettuate
FILE_TOTALI = "prenotazioni_totali.txt"

# siccome dopo voglio far scegliere di fare un altra prenotazione oppure vederle tutte
# Il while True tiene il programma in esecuzione finché
# l'utente non sceglie di uscire dal menu finale
while True:

    # Chiediamo il nome del paziente
    nome = input("\nInserisci il tuo nome: ")


    # Mostriamo le tipologie di visita disponibili
    print("Tipologie di visita disponibili:")
    print("1 - Visita generica")
    print("2 - Visita oculistica")
    print("3 - Visita cardiologica")
    print("4 - Visita dermatologica")

    scelta = input("Scegli il numero della visita: ")

    # In base al numero scelto, assegniamo il nome della visita
    match scelta:
        case "1":
            visita = "Visita generica"
        case "2":
            visita = "Visita oculistica"
        case "3":
            visita = "Visita cardiologica"
        case "4":
            visita = "Visita dermatologica"
        case _:
            # Qualsiasi altro valore non è valido
            visita = None

    if visita is None:
        print("Scelta non valida. Riprova.")
        # torna all'inizio del while
        continue

    # Chiediamo giorno e orario della prenotazione
    giorno = input("Inserisci il giorno (es. 15/05/2025): ")
    orario = input("Inserisci l'orario (es. 10:30): ")


# scrittura prenotazione

    print("Scrittura prenotazione ")

    # Costruiamo il nome del file usando nome, giorno e orario
    # formattazione per il nome file replace() rimuove i caratteri non validi per i nomi file (/ e :)
    nome_file = f"prenotazione_{nome}_{giorno.replace('/', '')}_{orario.replace(':', '')}.txt"

    # Apriamo il file in scrittura ("w") - viene creato se non esiste
    with open(nome_file, "w", encoding="utf-8") as f:
        f.write(f"Paziente: {nome}")
        f.write(f"Visita: {visita}")
        f.write(f"Giorno: {giorno}")
        f.write(f"Orario: {orario}")

    print(f"File '{nome_file}' salvato!")


    # riepilogo

    print("Riepilogo prenotazione")

    # Riapriamo il file in lettura e mostriamo il contenuto al paziente
    with open(nome_file, "r", encoding="utf-8") as f:
        contenuto = f.read()  # legge tutto il file in una volta
        print(contenuto)

    print("Prenotazione in attesa di conferma da parte dell'operatore...")


    # accettazione dall'operatore


    # L'operatore decide se confermare o annullare la prenotazione
    conferma = input("OPERATORE:  Confermare la prenotazione? (si/no): ")

    # In base alla risposta aggiorniamo lo stato
    match conferma.lower():
        case "si":
            stato = "CONFERMATA"
        case "no":
            stato = "ANNULLATA"
        case _:
            stato = "RISPOSTA NON VALIDA"

    # Aggiungiamo lo stato al file singolo senza cancellare i dati già scritti
    with open(nome_file, "a", encoding="utf-8") as f:
        f.write(f"Stato: {stato}")

    print(f"Prenotazione {stato}.")


  #scrittura file di riepilogo

    # Aggiungiamo la prenotazione al file generale con tutte le prenotazioni
    # Usiamo "a" così le prenotazioni precedenti non vengono cancellate
    
    if stato == "CONFERMATA":
        with open(FILE_TOTALI, "a", encoding="utf-8") as f:
            f.write(f"Paziente: {nome}")
            f.write(f"Visita: {visita}")
            f.write(f"Giorno: {giorno}")
            f.write(f"Orario: {orario}")
            f.write(f"Stato: {stato}")
            f.write("----------------------------")
        print(f"Prenotazione aggiunta a '{FILE_TOTALI}'.")
    else:
        # Se annullata o risposta non valida non viene registrata nel totale
        print("Prenotazione non registrata nel file totale.")
    


    # menu finale

    print("Cosa vuoi fare adesso?")
    print("1 - Visualizza tutte le prenotazioni")
    print("2 - Effettua un'altra prenotazione")
    print("3 - Esci")

    scelta_menu = input("Scegli: ")

    match scelta_menu:
        case "1":
            # Leggiamo e stampiamo il file con tutte le prenotazioni
            print("Tutte le prenotazioni ")
            with open(FILE_TOTALI, "r", encoding="utf-8") as f:
                print(f.read())
            # Dopo aver mostrato le prenotazioni il programma termina
            break
        case "2":
            # Torna all'inizio del while per una nuova prenotazione
            continue
        case _:
            # Qualsiasi altro tasto esce dal programma
            print("Arrivederci!")
            break