a = float(input('inserisci il primo numero:'))
b = float(input('inserisci il secondo numero:'))
operazione= input('inserisci l operazione da eseguire (+, -, *, /  ):')

match operazione:
    case '+':
        risultato = a + b
        print('il risultato è:', risultato)
    case '-':
        risultato = a - b
        print('il risultato è:', risultato)
    case '*':
        risultato = a * b
        print('il risultato è:', risultato)
    case '/':
        if b != 0:
            risultato = a / b
            print('il risultato è:', risultato)
        else:
            print('Errore: divisione per zero impossibile!')
            
            
