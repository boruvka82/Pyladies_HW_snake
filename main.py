from random import randrange

def nakresli_mapu(seznam_souradnic, seznam_ovoce):
    
    '''dostane seznam souřadnic a ovoce a vypíše je jako mapu 10x10'''
    znak = ['.']
    i = 10
    j = 10
    
    tabulka = []
    for seznam in range(i):
        seznam_znaku = znak * j
        tabulka.append(seznam_znaku)
    #print(tabulka)

    for ovoce in seznam_ovoce:
        tabulka[ovoce[1]][ovoce[0]] = "?"
    
    for souradnice in seznam_souradnic:
        tabulka[souradnice[1]][souradnice[0]] = "X"

    for seznam in tabulka:   
        print(' '.join(seznam), end = '\n')


def pohyb(seznam_souradnic, strana):
    '''fce dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a přidá k seznamu poslední bod „posunutý“ v daném směru''' 
    from random import randrange
    posledni_souradnice = seznam_souradnic[-1]
    
    if strana == 'v':
        souradnice_nova = (posledni_souradnice[0] + 1, posledni_souradnice[1])
    elif strana == 'z':
        souradnice_nova = (posledni_souradnice[0]- 1, posledni_souradnice[1])
    elif strana == 'j':
        souradnice_nova = (posledni_souradnice[0], posledni_souradnice[1]+ 1)
    elif strana == 's':
        souradnice_nova = (posledni_souradnice[0], posledni_souradnice[1]-1)

    if  0 <= souradnice_nova[0] <= 9 and 0 <= souradnice_nova[1] <= 9:
        if souradnice_nova in seznam_souradnic:
            raise ValueError('CHYBA! Souradnice jiz obsazena!')
        else:
            seznam_souradnic.append(souradnice_nova) #pohyb=>prida souradnic

            if souradnice_nova not in seznam_ovoce:
                #kdyz nesezere ovoce => pop zacatek
                seznam_souradnic.pop(0)
            else:
                #kdyz sezere, tak se neusekne hlava
                for ovoce in seznam_ovoce:
                    if ovoce in seznam_ovoce and ovoce in seznam_souradnic:
                        seznam_ovoce.remove(ovoce) #sezere,smaze se
                        if len(seznam_ovoce) == 0:  #neni ovoce, vytvori nahodne
                            vygeneruj_ovoce(seznam_souradnic,seznam_ovoce)
            print(seznam_souradnic)
            print('ovoce',seznam_ovoce)
                
    else:
        raise ValueError('CHYBA! Souradnice mimo tabulku!')
    
def vygeneruj_ovoce(seznam_souradnic, seznam_ovoce):
  '''nahodne vytvori ovoce pokud neni'''
    while True:
        a = randrange(10)
        b = randrange(10)
        ovoce_nove = (a,b)
        if ovoce_nove not in seznam_souradnic and ovoce_nove not in seznam_ovoce:
            seznam_ovoce.append(ovoce_nove)    #prida nahodne na prazdne policko, kde neni had
            return
          

#cyklus, který se bude ptát uživatele na světovou stranu, podle ní zavolá pohyb, a následně vykreslí seznam jako mapu
seznam_souradnic = [(0, 0), (1, 0), (2, 0)]
seznam_ovoce = [(2,3)]
pocet_kroku = 0

nakresli_mapu(seznam_souradnic, seznam_ovoce)
while True: 
    strana = input("Zadej svetovou stranu - s, j, v, z: ")
    
    if strana in ('s', 'j', 'v', 'z'):
        pohyb(seznam_souradnic, strana)   
        #po x krocich nahodne nove ovoce:
        pocet_kroku += 1
        print('pocet kroku:',pocet_kroku)
        if pocet_kroku % 30 == 0:        
            vygeneruj_ovoce(seznam_souradnic,seznam_ovoce)
        nakresli_mapu(seznam_souradnic,seznam_ovoce)
    else:
        print("spatne zadano:")
