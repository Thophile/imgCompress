# Encode un tableau de bit en utilisant l'encodage manchester (voir https://en.wikipedia.org/wiki/Manchester_code Section Encoding)
def b_to_manchester(b):
    #Nouvelle liste
    l = []
    #Pour chaque bit dans le tableau de bits
    for a in b:
        #ajouter a la liste le bit XOR 0 puis ajouté a la liste le bit XOR 1
        l.append(a ^ 0)
        l.append(a ^ 1)
    #Retourne la liste
    return l

# Decode un tableau de bit en utilisant l'encodage manchester
def manchester_to_b(manchester):
    #Nouvelle liste
    l = []
    #Booléen pour identifier chaque bit de la paire de bits
    first = True

    ## initialisation de la paire de bit
    t1 = 0
    t2 = 0

    #Pour chaque bit dans le tableau
    for a in manchester:
        #Si le Bit est le premier de la paire
        if first:
            #le premier bit prend la valeur bit XOR 0
            t1 = a ^ 0
            first = False
        #Si le Bit est le deuxième de la paire
        else :
            #le deuxieme bit prend la valeur bit XOR 1
            t2 = a ^ 1
            first = True

            #Si les deux bit sont identique , il n'y a pas d'erreur sur ce tick d'horloge
            if t1 == t2 :
                #ajouté la valeur a la liste
                l.append(t1)
    return l    

#Convertis un string en tableau de bit
def s_to_bitlist(s):
    #Créer un tableau contant un byte pour chaque caractère dans la chaine de caractère 
    ords = (ord(c) for c in s)
    #Tableau d'index des bit dans un byte
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    #ajoute chaque bit de chaque byte a un tableau de bit et le retourne
    return [(o >> shift) & 1 for o in ords for shift in shifts]

#Converti un tableau de bit en tableau de caractère
def bitlist_to_chars(bl):
    #Recupère l'itérateur du tableau
    bi = iter(bl)
    #Assemble chaque groupement de 8 bit en bytes et les stoque dans un tableau
    bytes = zip(*(bi,) * 8)
    #Tableau d'index des bit dans un byte
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    #Pour chaque byte dans le tableau de bytes
    for byte in bytes:
        #Retourne chaque byte converti en charactère (yield ajoute a chaque itération la valeur a un buffer de retour qui est retourné d'un seul coup)
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))

#Converti un tableau de caractère en string
def bitlist_to_s(bl):
    #
    return ''.join(bitlist_to_chars(bl))

#User input
s = input()

#Convert string to bit array
bitlist = s_to_bitlist(s)
print("\nInput to bits is :")
print(bitlist)

#Use Manchester XOR method to encode the bits
manchester = b_to_manchester(bitlist)
print("\nBits Manchester encoded is :")
print (manchester)

#Use Manchester XOR method to decode the bits
return_b = manchester_to_b(manchester)
print("\nManchester bits decoded is :")
print (return_b)

#Convert bit array to string
return_s = bitlist_to_s(return_b)
print("\nBits to String is :")
print (return_s)

