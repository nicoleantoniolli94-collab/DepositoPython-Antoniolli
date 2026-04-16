'''Scrivi un programma che esegua le seguenti operazioni:
1.Chiedi all'utente di inserire un numero intero positivo n. Se l'utente
inserisce un numero negativo o zero, continua a chiedere un numero fino a
quando non viene inserito un numero positivo.
2.Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza
della lista deve essere n.
3.Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella
lista.
4.Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
5.Utilizza un ciclo per determinare se un numero è primo. La funzione deve
restituire True se il numero è primo, altrimenti False.
6.Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
7.Infine, utilizza una struttura if per determinare se la somma di tutti i
numeri nella lista è un numero primo e stampa il risultato'''


while True:
   print('Scegli l esercizio da eseguire:')
   
   match(x):
       case 1: #inserimento numero positivo
           def inserisci_num_positivo():
                while True:
                     s = input("Inserisci un numero intero positivo: ")
                     if s.isdigit() and int(s) > 0:# controllo se è intero e positivo
                          return int(s)
                     else:
                          print("Input non valido. Inserisci un numero intero positivo (senza virgola).")
       case 2:
           
              n= inserisci_num_positivo()  #chiamata alla funzione per ottenere un numero positivo
              import random
              def genera_lista(n):
                 lista = []
                 for _ in range(n):
                        lista.append(random.randint(1, n))
                 return lista
             
       case 3:
              lista=genera_lista(n)  #chiamata alla funzione per generare la lista che ha al suo interno la richiesta del numero positivo
              def somma_pari(lista):
                 somma = 0
                 for numero in lista:
                      if numero % 2 == 0:
                            somma += numero
                 return somma
       case 4:
                lista=genera_lista(n)   #chiamata alla funzione per generare la lista che ha al suo interno la richiesta del numero positivo
                def stampa_dispari(lista):
                     for numero in lista:
                        if numero % 2 != 0:
                                print(numero)
       case 5:
              num= inserisci_num_positivo()  #chiamata alla funzione per ottenere un numero positivo
              def is_primo(num):
                 if num < 2:
                      return False
                 for i in range(2, int(num**0.5) + 1):
                      if num % i == 0:
                            return False
                 return True
       case 6:
           print('Esercizio 6')
       case 7:
           print('Esercizio 7')
           

    
