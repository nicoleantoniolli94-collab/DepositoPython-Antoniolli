#FUNZIONI

#1.Inserisci un numero intero positivo n. Se l'utente inserisce un numero negativo o zero, chiedi nuovamente l'input finché non viene inserito un numero valido.
def inserisci_num_positivo():
                while True: #ciclo infinito finché non viene inserito un numero positivo
                     n = input("Inserisci un numero intero positivo: ")
                     if n.isdigit() and int(n) > 0:# controllo se è intero e positivo
                          return int(n) #restituisco il numero convertito in intero
                     else:
                          print("Input non valido. Inserisci un numero intero positivo (senza virgola).")
                          
# 2 Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
import random
def genera_lista(n):
    lista = []
    for _ in range(n): #ciclo che si ripete n volte per generare n numeri casuali
        lista.append(random.randint(1, n)) #aggiungo alla lista un numero casuale tra 1 e n
    return lista #restituisco la lista generata


        
#5 Utilizza un ciclo per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False.
def è_primo(num):
                 
                 if num < 2:
                      return False
                 for i in range(2, int(num**0.5) + 1): #controllo se il numero è divisibile per qualche numero tra 2 e la radice quadrata di num
                      if num % i == 0: #se il numero è divisibile per i, allora non è primo
                            return False
                 return True
             
             
#3 Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
def somma_pari(lista):
                somma = 0 #variabile per tenere traccia della somma dei numeri pari
                for numero in lista:
                      if numero % 2 == 0:  #controllo se il numero è pari
                            somma += numero #aggiungo alla somma i numeri pari
                return somma  #restituisco la somma dei numeri pari
            
# MENU PRINCIPALE            
            
while True:
    x = input("Scegli un'operazione (1-7): ")
    if x.isdigit() and 1 <= int(x) <= 7:
        x = int(x)
        break
    else:
        print("Input non valido. Scegli un numero tra 1 e 7.")
   
   
match(x): #x è la variabile che contiene la scelta dell utente
       case 1: #inserimento numero positivo
               while inserisci_num_positivo(): 
                  print("Hai inserito un numero positivo.")
                  break
               else:
                print("Non hai inserito un numero positivo.")
               
           
       case 2: #2.Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
                print("Generazione di una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista sarà n.")
             #chiamata alla funzione per ottenere un numero positivo
                n = inserisci_num_positivo()
                lista = genera_lista(n)
                print("Lista generata con successo.")
                print(lista)
             
       case 3:#3.Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
               print("Calcolo della somma dei numeri pari nella lista generata.")
               n= inserisci_num_positivo()
               lista=genera_lista(n)  #chiamata alla funzione per generare la lista che ha al suo interno la richiesta del numero positivo
               print(f"La lista generata è: {lista}")
               print(f"La somma dei numeri pari nella lista è: {somma_pari(lista)}")
               
       case 4: #4.Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
           # qui non faccio una funzione a parte perché è un operazione molto semplice da fare direttamente nel case
                print("Stampa di tutti i numeri dispari nella lista generata.")
                n= inserisci_num_positivo()
                lista=genera_lista(n) 
                print(f"La lista generata è: {lista}")
                print("I numeri dispari nella lista sono: ", end="")
                for numero in lista:
                        if numero % 2 != 0:
                                 print(numero, end=" ") #stampo i numeri dispari separati da uno spazio
                print() #stampa una nuova linea dopo aver stampato tutti i numeri dispari 
       case 5: #5.Utilizza un ciclo per determinare se un numero è primo. La funzione deve restituire True se il numero è primo, altrimenti False.
              print("Verifica se un numero è primo.")
              num = inserisci_num_positivo()  #chiamata alla funzione per ottenere un numero positivo
              if è_primo(num):
                  print(f"{num} è un numero primo.")    
              else:
                  print(f"{num} non è un numero primo.")    
              
       case 6:  #6.Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
                    print("Stampa di tutti i numeri primi nella lista generata.")
                
                    n= inserisci_num_positivo()
                    lista=genera_lista(n)  #chiamata alla funzione per generare la lista che ha al suo interno la richiesta del numero positivo
                    print(f"La lista generata è: {lista}")
                    print("I numeri primi nella lista sono: ", end="")
                    for numero in lista:
                        if è_primo(numero): #chiamata alla funzione per verificare se il numero è primo
                                 print(numero, end=" ") #stampo i numeri primi separati da uno spazio
                                 print() #stampa una nuova linea dopo aver stampato tutti i numeri primi
           
       case 7: #7.Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato
                    print("Verifica se la somma di tutti i numeri nella lista è un numero primo.")
                    n= inserisci_num_positivo()
                    lista=genera_lista(n)  #chiamata alla funzione per generare la lista che ha al suo interno la richiesta del numero positivo
                    somma = sum(lista) #calcolo la somma di tutti i numeri nella lista
                    print(f"La lista generata è: {lista}")
                    if è_primo(somma): #chiamata alla funzione per verificare se la somma è un numero primo
                        print(f"La somma totale {somma} è un numero primo.")
                    else:
                        print(f"La somma totale {somma} non è un numero primo.")
           