# Classe base Posto
class Posto:
    def __init__(self, numero, fila):  # costruttore che riceve numero e fila
        self._numero = numero  # salviamo il numero del posto (privato)
        self._fila = fila      # salviamo la fila del posto (privato)
        self._occupato = False # di default il posto è libero (privato)

    def get_numero(self):  # getter per recuperare il numero
        return self._numero            

    def get_fila(self):# getter per recuperare la fila
        return self._fila               

    def get_occupato(self): # getter per recuperare lo stato
        return self._occupato         

    def prenota(self):                
        if not self._occupato:  # se il posto è libero (occupato è False)
            self._occupato = True # segniamo il posto come occupato
            print(f"Posto {self._numero} fila {self._fila} prenotato con successo!")
        else: # se il posto è già occupato
            print(f"Posto {self._numero} fila {self._fila} è già occupato!")

    def libera(self):# metodo per liberare il posto
        if self._occupato:# se il posto è occupato (occupato è True)
            self._occupato = False      # segniamo il posto come libero
            print(f"Posto {self._numero} fila {self._fila} liberato con successo!")
        else:                           # se il posto era già libero
            print(f"Posto {self._numero} fila {self._fila} non era prenotato!")


# Classe figlia PostoVIP - eredita da Posto e aggiunge servizi extra
class PostoVIP(Posto):
    def __init__(self, numero, fila): # costruttore
        super().__init__(numero, fila) # richiama il costruttore della madre
        self.servizi_extra = ["Accesso al lounge", "Servizio in posto"]  # lista dei servizi extra inclusi

    def prenota(self):                                                   # sovrascrive prenota() della madre
        if not self._occupato:                                           # se il posto è libero
            self._occupato = True                                        # segniamo il posto come occupato
            print(f"Posto VIP {self._numero} fila {self._fila} prenotato con successo!")
            print(f"Servizi extra attivati: {self.servizi_extra}")  # stampiamo i servizi attivati
        else: # se il posto è già occupato
            print(f"Posto VIP {self._numero} fila {self._fila} è già occupato!")


# Classe figlia PostoStandard - eredita da Posto e aggiunge un costo
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):  # costruttore che riceve anche il costo
        super().__init__(numero, fila)         # richiama il costruttore della madre
        self.costo = costo                     # salviamo il costo della prenotazione

    def prenota(self):                         # sovrascrive prenota() della madre
        if not self._occupato:                 # se il posto è libero
            self._occupato = True              # segniamo il posto come occupato
            print(f"Posto Standard {self._numero} fila {self._fila} prenotato con successo!")
            print(f"Costo prenotazione: €{self.costo}")  # stampiamo il costo
        else: # se il posto è già occupato
            print(f"Posto Standard {self._numero} fila {self._fila} è già occupato!")


# Classe Teatro che gestisce tutti i posti
class Teatro:
    def __init__(self):          # costruttore
        self._posti = []         # lista vuota che conterrà tutti i posti

    def aggiungi_posto(self, posto):   # metodo per aggiungere un posto alla lista
        self._posti.append(posto)      # aggiungiamo il posto alla lista

    def prenota_posto(self, numero, fila):          
        for posto in self._posti:# scorriamo tutti i posti
            if posto.get_numero() == numero and posto.get_fila() == fila:  # se troviamo il posto
                posto.prenota() # chiamiamo prenota() - polimorfismo: VIP o Standard si comportano diversamente
                return # usciamo dal metodo
        print(f"Posto {numero} fila {fila} non trovato!")  # se non troviamo il posto

    def libera_posto(self, numero, fila):# metodo per liberare un posto
        for posto in self._posti:                   # scorriamo tutti i posti
            if posto.get_numero() == numero and posto.get_fila() == fila:  # se troviamo il posto
                posto.libera() # chiamiamo libera()
                return                              # usciamo dal metodo
        print(f"Posto {numero} fila {fila} non trovato!")  # se non troviamo il posto

    def stampa_posti_occupati(self):    # metodo per stampare tutti i posti occupati
        print("Posti occupati")
        trovati = False # flag per sapere se ci sono posti occupati
        for posto in self._posti:       # scorriamo tutti i posti
            if posto.get_occupato():    # se il posto è occupato
                # controlliamo il tipo
                if isinstance(posto, PostoVIP) :
                   tipo= 'VIP'
                else :
                    tipo = 'Standard'
                print(f"Posto {posto.get_numero()} fila {posto.get_fila()} ({tipo})")  # stampiamo il posto
                trovati = True          # aggiorniamo il flag
        if not trovati:# se non abbiamo trovato nessun posto occupato
            print("Nessun posto occupato.")

    def stampa_tutti_posti(self):  # metodo per stampare tutti i posti
        print("Tutti i posti ")
        for posto in self._posti:  # scorriamo tutti i posti
            tipo = "VIP" if isinstance(posto, PostoVIP) else "Standard"  # controlliamo il tipo
            print(f"Posto {posto.get_numero()} fila {posto.get_fila()} ({tipo})")  # stampiamo


# --- Programma principale ---

teatro = Teatro()                                    # creiamo il teatro
teatro.aggiungi_posto(PostoVIP(1, "A"))              # aggiungiamo posto VIP numero 1 fila A
teatro.aggiungi_posto(PostoVIP(2, "A"))              # aggiungiamo posto VIP numero 2 fila A
teatro.aggiungi_posto(PostoStandard(1, "B", 5.50))   # aggiungiamo posto Standard numero 1 fila B costo €5.50
teatro.aggiungi_posto(PostoStandard(2, "B", 5.50))   # aggiungiamo posto Standard numero 2 fila B costo €5.50
teatro.aggiungi_posto(PostoStandard(1, "C", 3.00))   # aggiungiamo posto Standard numero 1 fila C costo €3.00
teatro.aggiungi_posto(PostoStandard(2, "C", 3.00))   # aggiungiamo posto Standard numero 2 fila C costo €3.00






while True:  # ciclo che continua finché l'utente non sceglie di uscire
    teatro.stampa_tutti_posti()

    print("--- Menu Teatro ---")
    print("1 - Prenota un posto")
    print("2 - Libera un posto")
    print("3 - Mostra posti occupati")
    print("4 - Esci")

    scelta = input("Scegli un'opzione: ")  # leggiamo la scelta dell'utente

    match scelta:                            
        case "1":     #scelta posto per prenotare                    
            fila = input("Inserisci la fila (A, B, C): ").upper()   # leggiamo la fila e la mettiamo in maiuscolo
            numero = int(input("Inserisci il numero del posto: "))   # leggiamo il numero e lo convertiamo in intero
            teatro.prenota_posto(numero, fila)                       # chiamiamo prenota_posto() sul teatro

        case "2":    #scelta posto per disdire                
            fila = input("Inserisci la fila (A, B, C): ").upper()   # leggiamo la fila e la mettiamo in maiuscolo
            numero = int(input("Inserisci il numero del posto: "))   # leggiamo il numero e lo convertiamo in intero
            teatro.libera_posto(numero, fila)                        # chiamiamo libera_posto() sul teatro

        case "3":                           
            teatro.stampa_posti_occupati()   # stampiamo tutti i posti occupati

        case "4":                            
            print("Arrivederci!")            # salutiamo l'utente
            break                            # usciamo dal ciclo while

        case _:                              # qualsiasi altro valore (default)
            print("Scelta non valida!")      # segnaliamo che la scelta non è valida