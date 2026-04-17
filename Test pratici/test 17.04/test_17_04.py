

# variabbili globali

utenti = []



# BLOCCO 0 — Variabili globali

utenti = []
lista_numeri = []
risultati = []


# BLOCCO 1 — Login / Registrazione

loggato = False # variabile di controllo per il ciclo di login/registrazione

while not loggato:  
    print("digita il numero dell'opzionne che vuoi eseguire:")
    print("1. Login")
    print("2. Registrati")
    
    
    scelta = input("Scegli: ").strip().lower() #la scelta dell'utente viene convertita in minuscolo e spazi rimossi per evitare errori di input
    
    match scelta:
        case "1": # Login, chiedo nome e password 
            nome = input("Nome utente: ").strip().lower()
            password = input("Password: ").strip()
            
            esiste = False  #controllo se nome e password esistono nella lista degli utenti
            for utente in utenti: #scorro la lista degli utenti 
                if utente["nome"] == nome and utente["password"] == password:
                    esiste = True
                    break
            
            if esiste:
                print(f" Benvenut {nome}! :) ")
                loggato = True
            else:
                print("Credenziali errate, riprova. oppure registrati se non hai un account.") # aggiungi il ritorno al menu principale per permettere all'utente di scegliere se fare login o registrarsi
            
        
        case "2":
            nome = input("Scegli un nome utente: ").strip().lower()
            
            esiste = False #controllo se il nome utente scelto esiste già nella lista degli utenti
            for utente in utenti:
                if utente["nome"] == nome:
                    esiste = True
                    break
            
            if esiste:
                print("Nome già in uso, scegline un altro.")
            else:
                password = input("Scegli una password: ").strip()
                utenti.append({"nome": nome, "password": password})
                print("Registrazione completata! Ora puoi fare il login.")
        
        case _:
            print("Scelta non valida.")
            
            
#chiedi all'utente di inserire un numero e salvali nella lista . Continua a chiedere finché l'utente non decide di smettere solo se la lista è maggiore di due elementi, poi stampa la lista dei numeri inseriti.

lista = [] #lista globale per salvare i numeri inseriti dall'utente

# FUNZIONI

def compila_lista():# funzione che faccio partire prima dei menu
    while True:
        numero = float(input("Inserisci un numero: "))
        lista.append(numero) #aggiungo il numero inserito alla lista 

        scelta = input("Vuoi inserire un altro numero? (si/no): ").lower()
        if scelta == "no": # solo se la lista è maggiore di due elementi
            if len(lista) > 2:
                break
            #se numero = parola non lo prende quindi chiedo di inserire un numero valido
            elif not isinstance(numero, int): 
                print("Input non valido. Inserisci un numero.")
                continue
            else:
                print("Devi inserire almeno 3 numeri prima di poter smettere.")
                continue
    print("Hai inserito i seguenti numeri:", lista)
    
def somma_pari(lista):
    somma = 0 #variabile per tenere traccia della somma dei numeri pari
    for numero in lista:
        if numero % 2 == 0:  #controllo se il numero è pari
            somma += numero #aggiungo alla somma i numeri pari
    return somma  #restituisco la somma dei numeri pari

def sottrazione(lista):
    sottrazione = lista[0] #prendo il primo numero della lista come punto di partenza per la sottrazione, se no andrebbe già sotto zero al primo ciclo
    for numero in lista[1:]: #scorro la lista a partire dal secondo elemento
        sottrazione -= numero #sottraggo ogni numero al risultato
    return sottrazione #restituisco il risultato finale della sottrazione

def moltiplicazione(lista):
    moltiplicazione = 1 #prendo 1 come punto di partenza per la moltiplicazione, se no andrebbe già a zero al primo ciclo
    for numero in lista:
        moltiplicazione *= numero #moltiplico ogni numero al risultato
    return moltiplicazione #restituisco il risultato finale della moltiplicazione

def divisione(lista):
    divisione = lista[0] #prendo il primo numero della lista come punto di partenza per la divisione, se no andrebbe già a zero al primo ciclo
    for numero in lista[1:]: #scorro la lista a partire dal secondo elemento
        if numero != 0: #controllo che il numero non sia zero per evitare errori di divisione per zero
            divisione /= numero #divido ogni numero al risultato
        else:
            print("Errore: divisione per zero. Ignorando questo numero.")
    return divisione #restituisco il risultato finale della divisione

def media(lista):
    if len(lista) > 0: #controllo che la lista non sia vuota per evitare errori di divisione per zero
        media = sum(lista) / len(lista) #calcolo la media come somma dei numeri divisa per il numero di elementi nella lista
        return media #restituisco la media
    else:
        print("La lista è vuota, impossibile calcolare la media.")
        return None #restituisco None se la lista è vuota
    
 
 
#richiamo la funzione per compilare la lista dei numeri
compila_lista()   
    
# MENU PRINCIPALE
while True:
    print("\n--- MENU PRINCIPALE ---")
    print("1. Calcolatrice")
    print("2. Storico")
    print("x. Logout")
    
    scelta = input("Scegli: ").strip().lower()
    
    match scelta:
        
        case "1": # MENU CALCOLATRICE
            contatore = 0
            while contatore < 4: #l'utente può eseguire solo 4 operazioni, poi deve riloggarsi
                print("\n MENU CALCOLATRICE")
                print("1. Somma")
                print("2. Sottrazione")
                print("3. Moltiplicazione")
                print("4. Divisione")
                print("5. Media")
                
                scelta = input("Scegli: ").strip().lower()
                
                match scelta:
                    case "1":
                        print(f"Lista dei numeri che hai scelto è : {lista}")
                        print(f"Risultato della somma dei nummeri pari della lista è : {somma_pari(lista)}")
                        contatore += 1
                    case "2":
                        print(f"Lista dei numeri che hai scelto è : {lista}")
                        print(f"Risultato sottrazione: {sottrazione(lista)}")
                        contatore += 1
                    case "3":
                        print(f"Lista dei numeri che hai scelto è : {lista}")
                        print(f"Risultato moltiplicazione: {moltiplicazione(lista)}")
                        contatore += 1
                    case "4":
                        print(f"Lista dei numeri che hai scelto è : {lista}")
                        print(f"Risultato divisione: {divisione(lista)}")
                        contatore += 1
                    case "5":
                        print(f"Lista dei numeri che hai scelto è : {lista}")
                        print(f"Risultato media: {media(lista)}")
                        contatore += 1
                    case _:
                        print("Scelta non valida.")
            
            print("Hai eseguito 4 operazioni, devi riloggarti!")
            loggato = False
            break   # controlliamo se tutto funziona 
        
        case "2":
            while True:
                print("\n--- MENU STORICO ---")
                print("1. Stampa lista numeri")
                print("x. Torna al menu principale")
                
                scelta = input("Scegli: ").strip().lower()
                
                match scelta:
                    case "1":
                        print(f"Lista numeri: {lista}")
                    case "x":
                        break
                    case _:
                        print("Scelta non valida.")
        
        case "x":
            print("Logout effettuato.")
            loggato = False
            break
        
        case _:
            print("Scelta non valida.")




            
            