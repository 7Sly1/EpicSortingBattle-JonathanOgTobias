import random, sys
from inspect import getmembers


def insertionSort(items):
    items = items.copy()
    for i in range(1,len(items)):
        # Her laver vi variabelerne "index" og "index2", hvor index2 gemmer på placering i vores liste.
        # Og index gemmer på pladsen bag index2.
        index2 = items[i]
        index = i - 1
        '''Her laver vi et "While Loop",
        som tjekker at index enten er større eller lige 0,
        samt at "index2" i vores liste forbliver mindre end vores index i listen.'''
        while index >= 0 and index2 < items[index]:
            '''Hvis vores betingelser for det "While Loop" er sande,
            så får vi koden til at bytte index plads med den foran.'''
            items[index + 1] = items[index]
            #Efter at de to værdier har bytte plads,
                #sætter vi index tilbage på dets gamle plads.
            index -= 1
        #Her hopper vi en plads mere frem i vores liste
        items[index + 1] = index2
    #Når vi er færdige retunere vi listen "items", i korrekt sorteret rækkefølge
    return items



def bubbleSort(items):
    items = items.copy()
    n = len(items)
    # Her definere vi vores længde af listen "Items".
    for i in range(n - 1):
        # Her laver vi variabelen "index" i et "for loop", som er sat til at ligge en plads bagved det vi er nået til
        # i vores liste
        for index in range(0, n - i - 1):
            # Her tjekker vi om de 2 elementer vi sammenligner står i korrekt rækkefølge.
            if items[index] > items[index+1]:
                # Hvis ikke, så bytter vi rundt på de 2 elementer.
                items[index], items[index+1] = items[index+1], items[index]
    # Her returnere vi listen "items" i korrekt i sorteret rækkefølge
    return items



if __name__ == '__main__':

    functions = [] # Liste til funktioner vi gerne vil teste

    for function in getmembers(sys.modules[__name__]): # Får alle funktioner i denne fil
        if 'Sort' in function[0]: # Finder "sort" i functionen
            functions.append(function) # Appender de fundne funktioner til en liste så vi kan iterate over dem

    for sort in functions:
        l = list(range(0, 10)) # Laver en tilfældig liste
        lb = l.copy() # Kopierer listen for at bevare den originale
        for i in range(50): # Prøver at sortere den
            random.shuffle(lb)
            ls = sort[1](l)
            if ls != l:
                print(f'\nFejl! {sort[0]} Algoritmen kan ikke sortere.')
                break
        print(f'\nSucces! {sort[0]} Algoritmen sorterer korrekt.')
        print('blandet: ', lb)
        print('sorteret:', ls)

