


import random, copy

def bogoSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Giver op på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items

def insertionSort(items):
    # Her tager vi listen "Items" som var vedlagt i opgaven.
    items = items.copy()
    # Her definere vi vores længde af listen "Items".
    for i in range(0,len(items)):
        # Her laver vi variabelen "index", den er sat til at ligge en plads bagved "i".
        index = i - 1
        '''Her laver vi et "While Loop",
        som tjekker at index enten er større eller lige 0,
        samt at i vores liste forbliver mindre end vores index i listen.'''
        while index >= 0 and i < items[index]:

            items[index + 1] = items[index]

            index -= 1

        items[index + 1] = i

    return items


def bubbleSort(items):
    # Her tager vi listen "Items" som var vedlagt i opgaven.
    items = items.copy()
    # Her definere vi vores længde af listen "Items".
    for i in range(0,len(items)):
        # Her laver vi variabelen "index", den er sat til at ligge en plads bagved "i".
        for index in range(0,len(items)-i-1):
            # Her laver vi et tjek om de 2 elementer vi sammenligner står i korrekt rækkefølge.
            if items[index] > items[index + 1]:
                # Hvis ikke, så bytte vi rundt på de 2 elementer.
                items[index], items[index + 1] = items[index + 1], items[index]
    # Her returnere vi listen "items" i korrekt i sorteret rækkefølge
    return items


if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = bubbleSort(lb)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)


