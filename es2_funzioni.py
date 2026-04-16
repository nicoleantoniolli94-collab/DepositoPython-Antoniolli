# Tupla con la sequenza di Fibonacci predefinita
fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987)
 
 
def stampa_fibonacci(n):
    # Scorre tutti i numeri della tupla
    for numero in fibonacci:
        # Stampa solo i numeri minori o uguali a N
        if numero <= n:
            print(numero)
 
 
# Chiede all'utente il limite massimo
n = int(input("Inserisci un numero N: "))
# Chiama la funzione passando il numero inserito
stampa_fibonacci(n)





