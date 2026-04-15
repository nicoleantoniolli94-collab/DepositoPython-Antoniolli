
#Creare un if con else semplice, dentro l’if inserire una strttura di
#creazione di dati ( nome, password, id dato dal sistema a crescere  ) e
#nell’else il controllo automatico la dove è presente l’accout nel sistema
#e solo se si passa dall’else concludere lo script

utente= ['nicole', '1234', 1 ]

print('Hai un account?')
risposta = input('digita si o no:')

if risposta == 'si':
    nome = input('inserisci il tuo nome:')
    password = input('inserisci la tua password:')
    if nome == utente[0] and password == utente[1]:
        print('Accesso riuscito!')
    else:
        print('Nome o password errati!')
elif risposta == 'no':
    print('Creazione account')
    nome = input('inserisci il tuo nome:')
    password = input('inserisci la tua password:')
    if nome != utente[0] and password != utente[1]:
        utente_nuovo= [nome, password, utente[2]+1]
        print('Account creato con successo!')
        
        

    
   

