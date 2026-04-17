


# BLOCCO 0 — Variabili globali

utenti = []          
            
#chiedi all'utente di inserire un numero e salvali nella lista . 
# Continua a chiedere finché l'utente non decide di smettere solo se la lista è maggiore di due elementi, poi stampa la lista dei numeri inseriti.

lista = [] #lista globale per salvare i numeri inseriti dall'utente

# FUNZIONI

# funzione inserimento numeri nella lista
def compila_lista():# funzione che farò partire prima dei menu
    print('ora crea la tua lista di numeri! ')
    while True: # ciclo infinito finché l'utente non decide di smettere e la lista è maggiore di 2 elementi
        valore = input("Inserisci un numero: ")
        
        if not valore.isdigit(): #controllo se l'input è un numero intero , se no mostro un messaggio di errore e continuo il ciclo
            print("Input non valido. Inserisci un numero intero.")
            continue
        
        numero = int(valore)  #Cconverto l'input in un numero intero e lo aggiungo alla lista
        lista.append(numero)

        while True: # ciclo infinito finché l'utente non decide di smettere, se la lista è maggiore di 2 elementi
            scelta = input("Vuoi inserire un altro numero? (si/no): ").lower()
            if scelta == "si": #gestisco le due scelte 
                break # se l'utente vuole inserire un altro numero, esco da questo ciclo e torno al ciclo principale per chiedere un altro numero
            elif scelta == "no": # se l'utente non vuole inserire un altro numero, controllo se la lista è maggiore di 2 elementi, se si esco dal ciclo principale, altrimenti errore e continuo a chiedere se vuole inserire un altro numero
                if len(lista) > 2:
                    break # se vero esco 
                else:
                    print("Devi inserire almeno 3 numeri prima di poter smettere.") # se falso e richiedo il numero
            else:
                print("Input non valido. Digita 'si' o 'no'.") 
        
        if scelta == "no" and len(lista) > 2:
            break

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
    divisione = lista[0] #prendo il primo numero della lista come punto di partenza per la divisione, se no andrebbe già a zero al primo ciclo e non avrebbe senso dividere per zero
    for numero in lista[1:]: #scorro la lista a partire dal secondo elemento
        if numero != 0: #controllo che il numero non sia zero per evitare errori di divisione per zero
            divisione /= numero #divido ogni numero al risultato
        else:
            print("Errore: nella tua lista c'è uno zero e non si può dividere per zero :( )")
    return divisione #restituisco il risultato finale della divisione

def media(lista):
    if len(lista) > 0: #controllo che la lista non sia vuota per evitare errori di divisione per zero ma in teoria non dovrebbe essere vuota perché l'utente deve inserire almeno 3 numeri, ma è sempre meglio mettere un controllo per evitare errori imprevisti
        media = sum(lista) / len(lista) #calcolo la media come somma dei numeri divisa per il numero di elementi nella lista
        return media #restituisco la media
    else:
        print("La lista è vuota, impossibile calcolare la media.")
        return None #restituisco None se la lista è vuota
    
print("Benvenutə alla tua calcolatrice! Prima di iniziare, devi fare il login o registrarti.")   

while True:   # ciclo principale del programma, finché l'utente non decide di uscire
              

    loggato = False # variabile di controllo per il ciclo di login/registrazione

    while not loggato:  # finché l'utente non è loggato, mostro il menu di login/registrazione
                        # quando l'utente si slogga (nel menu principale e nel menu calcolatrice dopo 4 tentativi ) il programma torna qui
       
       
        print("digita il numero dell'opzionne che vuoi eseguire:")
        print("1. Login")
        print("2. Registrati")
        
        #l utente digita l opzione che vuole eseguire
        scelta = input("Scegli: ").strip().lower() #la scelta dell'utente viene convertita in minuscolo e spazi rimossi per evitare errori 
        
        match scelta: #match per gestire login e registrazione 
            case "1": # Login, chiedo nome e password 
                nome = input("Nome utente: ").strip().lower()
                password = input("Password: ").strip()
                
                esiste = False  #controllo se nome e password esistono nella lista degli utenti
                for utente in utenti: #scorro la lista degli utenti e se trovo una corrispondenza con nome e password, allora esiste setto  esiste = True e posso uscire dal ciclo
                    if utente["nome"] == nome and utente["password"] == password:
                        esiste = True
                        break
                
                if esiste: # se esiste è true, allora setto loggato= true e posso uscire dal ciclo di login/registrazione
                    print(f" Benvenutə {nome}! :) ") 
                    loggato = True
                else: #se esiste è false allora nome o password sono errati, mostro un messaggio di errore e rimando al menu di login/registrazione
                    print("Credenziali errate, riprova. oppure registrati se non hai un account.") # ritorna al menu di login/registrazione
                
            
            case "2": # Registrazione, chiedo nome e password e li salvo nella lista degli utenti se il nome non è già in uso
                nome = input("Scegli un nome utente: ").strip().lower()
                
                esiste = False #controllo se il nome utente scelto esiste già nella lista degli utenti
                for utente in utenti: #itera sulla lista utenti e se trova corrispondenza setta esiste a True e esce dal ciclo e passo
                    if utente["nome"] == nome:
                        esiste = True
                        break
                # se esiste o non esiste:
                if esiste: # se esiste  = true evita di inserire utenti gia esistenti
                    print("Nome già in uso, scegline un altro.")
                else: # se esiste = false allora il nome è disponibile, chiedo la password e salvo il nuovo utente nella lista degli utenti
                    password = input("Scegli una password: ").strip()
                    utenti.append({"nome": nome, "password": password})
                    print("Registrazione completata! Ora puoi fare il login oppure creare un altro account.")
            
            case _: # se la scelta non è 1 o 2, mostro un messaggio di errore 
                print("Scelta non valida.")
    
    lista = [] #resetto la lista dei numeri ogni volta che un utente si logga, cos' se esce e rientra non ha anche i nuemri inseriti nella sessione preccedente
    #richiamo la funzione per compilare la lista dei numeri
    compila_lista()   
        
    # MENU PRINCIPALE
    while True: 
        print("\n---MENU PRINCIPALE ---")
        print("1. Calcolatrice")
        print("2. Riepilogo")
        print("x. Logout")
        
        scelta = input("Scegli: ").strip().lower()
        
        match scelta:
            
            case "1": # MENU CALCOLATRICE
                contatore = 0
                while contatore < 4: #l'utente può eseguire solo 4 operazioni, poi deve riloggarsi
                    print("\n MENU CALCOLATRICE")
                    print("1. Somma numeri pari")
                    print("2. Sottrazione")
                    print("3. Moltiplicazione")
                    print("4. Divisione")
                    print("5. Media")
                    
                    scelta = input("Scegli: ").strip().lower()
                    
                    match scelta:
                        case "1": #SOMMA NUMERI PARI
                            print(f"Lista dei numeri che hai scelto è : {lista}")
                            print(f"Risultato della somma dei nummeri pari della lista è : {somma_pari(lista)}") #chiamo la funzione somma_pari che prende in input la lista dei numeri e restituisce la somma dei numeri pari, poi stampo il risultato
                            contatore += 1 # incremento il contatore ogni volta che l'utente esegue un'operazione, quando arriva a 4 esce dal ciclo e deve riloggarsi
                        case "2": #SOTTRAZIONE
                            print(f"Lista dei numeri che hai scelto è : {lista}")#stampo la lista dei numeri che l'utente ha scelto prima di eseguire l'operazione, così può vedere i numeri su cui sta operando
                            print(f"Risultato sottrazione: {sottrazione(lista)}")#chiamo la funzione sottrazione che prende in input la lista dei numeri e restituisce il risultato della sottrazione, poi stampo il risultato
                            contatore += 1 # incremento il contatore ogni volta che l'utente esegue un'operazione, quando arriva a 4 esce dal ciclo e deve riloggarsi
                        case "3":# MOLTIPLICAZIONE
                            print(f"Lista dei numeri che hai scelto è : {lista}")
                            print(f"Risultato moltiplicazione: {moltiplicazione(lista)}")
                            contatore += 1
                        case "4": #DIVISIONE
                            print(f"Lista dei numeri che hai scelto è : {lista}")
                            print(f"Risultato divisione: {divisione(lista)}")
                            contatore += 1
                        case "5": #MEDIA
                            print(f"Lista dei numeri che hai scelto è : {lista}")
                            print(f"Risultato media: {media(lista)}")
                            contatore += 1
                        case _:
                            print("Scelta non valida.")
                
                print("Hai già eseguito 4 operazioni :(  devi riloggarti!")
                loggato = False #settando loggato falso interrompo il ciclo del menu principale e torno al ciclo di login/registrazione
                break   # controlliamo se tutto funziona 
            
            case "2": # MENU RIEPILOGO
                while True:
                    print("\n--- MENU RIEPILOGO ---")
                    print("1. Stampa lista numeri")
                    print("2. Stampa risultato di tutte le operazioni della calcolatrice")
                    print("x. Torna al menu principale")
                    
                    scelta = input("Scegli: ").strip().lower()
                    
                    match scelta:
                        case "1": # STAMPA LISTA NUMERI
                            print(f"Lista numeri: {lista}")
                        case "2": # STAMPA RISULTATO DI TUTTE LE OPERAZIONI DELLA CALCOLATRICE
                            print(f"Lista dei numeri che hai scelto è : {lista}")
                            print(f"Risultato somma dei numeri pari: {somma_pari(lista)}")
                            print(f"Risultato della sottrazione dei numeri nella tua lista: {sottrazione(lista)}")
                            print(f"Risultato della moltiplicazione dei numeri nella tua lista: {moltiplicazione(lista)}")
                            print(f"Risultato della divisione dei numeri nella tua lista: {divisione(lista)}")
                            print(f"Risultato della media dei numeri nella tua lista: {media(lista)}")
                        case "x": # TORNA AL MENU PRINCIPALE
                            break # chiude questo match e torna al menu principale
                        case _: #ERRORE
                            print("Scelta non valida.")
            
            case "x": # LOGOUT
                print("Logout effettuato.")
                loggato = False # anche qui settando loggato falso interrompo il ciclo del menu principale e torno al ciclo di login/registrazione
                break
            
            case _:
                print("Scelta non valida.")




            
            