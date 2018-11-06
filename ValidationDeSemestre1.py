moyenne_UE1 = int(input("Saisir la moyenne de l'UE 1 : "))
moyenne_UE2 = int(input("Saisir la moyenne de l'UE 2 : "))

moyenne_generale = (moyenne_UE1 + moyenne_UE2)/2

#CAS 1:
#Tong diem lon hon hoac bang 20 va ko co UE nao nho hon 8:

_tous_les_UE_sup8 = False
_moyenne_generale_sup20 = False

if (moyenne_UE1 >= 8 && moyenne_UE2 >= 8):
    _tous_les_UE_sup8 = True

if (moyenne_generale >= 20):
    _moyenne_generale_sup20 =True



#CAS 2: