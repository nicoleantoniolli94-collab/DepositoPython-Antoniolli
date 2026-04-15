# menu con aggiungi modifica elimina, selezione tramite if

# stringa [elimina, aggiungi, modifica]

menu = ['elimina', 'aggiungi', 'modifica']
print('Benvenuto nel menu!')
selezione = input('digita un opzione (elimina, aggiungi, modifica):')

invitati = ['Caterina', 'Richard', 'Marco', 'Jenny', 'Luca']

'''if selezione == 'elimina':
    print('hai selezionato elimina')
elif selezione == 'aggiungi':
    print('hai selezionato aggiungi')
elif selezione == 'modifica':
    print('hai selezionato modifica')
else:
    print('opzione non valida') '''


if selezione == menu[0]:
    eliminare_invitato = input('inserisci il nome dell\'invitato da eliminare:')
    if eliminare_invitato in invitati:
        invitati.remove(eliminare_invitato)
        print('l\'invitato', eliminare_invitato , 'è stato eliminato')
    else:
        print('invitato non trovato')
elif selezione == menu[1]:
    nuovo_invitato = input('inserisci il nome del nuovo invitato da aggiungere:')
    invitati.append(nuovo_invitato)
    print('l\'invitato' , nuovo_invitato , 'è stato aggiunto')
elif selezione == menu[2]:
    vecchio_invitato = input('inserisci il nome dell\'invitato da modificare:')
    if vecchio_invitato in invitati:
        nuovo_invitato = input('inserisci il nuovo nome dell\'invitato:')
        indice = invitati.index(vecchio_invitato)
        invitati[indice] = nuovo_invitato
        print('l\'invitato', vecchio_invitato , 'è stato modificato in', nuovo_invitato)
    else:
        print('invitato non trovato')
else:
    print('opzione non valida')