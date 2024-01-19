
sbox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 0xe, 0xf, 8, 4, 7, 1, 2]
nbox = [sbox.index(i) for i in range(16)]

def round(k, s):
    return sbox[k ^ s]

def enc(k, m) :
    t = round(k[0], m)
    c = round(k[1], t)
    return c

def back_round(k, s):
    sb = nbox[s]
    return sb ^ k

def dec(k, m):
    t = back_round(k[1], m)
    c = back_round(k[0], t)
    return c

def enc_byte(key, m):
    nibble1 = m >> 4
    nibble2 = m & 0b1111
    
    nibble1 = enc(key, nibble1)
    nibble2 = enc(key, nibble2)
    
    message_chiffre = (nibble1 << 4) | nibble2
    
    return message_chiffre

def dec_byte(key, m):
    nibble1 = m >> 4
    nibble2 = m & 0b1111
    
    nibble1 = dec(key, nibble1)
    nibble2 = dec(key, nibble2)
    
    message_dechiffre = (nibble1 << 4) | nibble2
    
    return message_dechiffre

def enc_texte_cbc(k, texte, vecteur):

    texte_chiffre = ''
    texte_chiff = vecteur

    for i in texte:
        caractere = ord(i)
        texte_chiff = texte_chiff ^ caractere
        texte_chiff = enc_byte(k, texte_chiff)
        texte_chiffre += chr(texte_chiff)

    return texte_chiffre


def dec_texte_cbc(k, texte, vecteur):

    texte_dechiff = ''
    texte_avant = vecteur

    for i in texte:
        texte_dechiffre = dec_byte(k, ord(i))
        texte_dechiffre = texte_dechiffre ^ texte_avant
        texte_dechiff += chr(texte_dechiffre)
        texte_avant = ord(i)

    return texte_dechiff