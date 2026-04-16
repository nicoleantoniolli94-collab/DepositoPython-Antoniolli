# Tupla con la sequenza di Fibonacci predefinita
fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
 
 
def Fibonacci_minore_di(n):
    # Restituisce una lista con i numeri di Fibonacci minori o uguali a N
    risultato = []
    for numero in fibonacci:
        if numero <= n:
            risultato.append(numero)
    return risultato
 
 
# Chiede all'utente il limite massimo
n = int(input("Inserisci un numero N: "))
# Chiama la funzione e stampa il risultato
print(Fibonacci_minore_di(n))